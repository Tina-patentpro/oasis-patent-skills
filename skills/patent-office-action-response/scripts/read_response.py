"""Read a same-file M14 canonical response into an explicit legacy core view.

Does not decide technical completeness, legality, or path validity.
Outputs are exclusive-created; the source is never rewritten.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

def digest(data):
    return hashlib.sha256(data).hexdigest()

def headings_outside_fences(text):
    """Keep original match offsets while excluding ordinary fenced quotations."""
    fenced_starts = set()
    fence = None
    offset = 0
    for line in text.splitlines(keepends=True):
        content = line.rstrip('\r\n')
        if fence is not None:
            fenced_starts.add(offset)
            char, length = fence
            if re.fullmatch(r' {0,3}' + re.escape(char) + r'{' + str(length) + r',}[ \t]*', content):
                fence = None
        else:
            opening = re.fullmatch(r' {0,3}(`{3,}|~{3,})(.*)', content)
            if opening and not (opening[1][0] == '`' and '`' in opening[2]):
                fence = (opening[1][0], len(opening[1]))
                fenced_starts.add(offset)
        offset += len(line)
    return [match for match in re.finditer(r'^## (.+)\s*$', text, re.M)
            if match.start() not in fenced_starts]

def project(text):
    headings = headings_outside_fences(text)
    names = [m.group(1).strip() for m in headings]
    expected = ['文档信息', '核心结论', '核心结果', '下游读取区', '风险与待确认事项']
    if names != expected:
        raise ValueError('Expected exactly five ordered main sections')
    core_start, core_end = headings[2].end(), headings[3].start()
    down_start, down_end = headings[3].end(), headings[4].start()
    core = text[core_start:core_end]
    blocks = {}
    for path in 'abc':
        ref = '<!-- m14-core-path-' + path + ' -->'
        start = '<!-- m14-path-' + path + ':start -->'
        end = '<!-- m14-path-' + path + ':end -->'
        anchor = '<a id="m14-path-' + path + '"></a>'
        if any(text.count(marker) != 1 for marker in (ref, start, end, anchor)):
            raise ValueError('Missing or repeated path marker: ' + path)
        ri, si, ei, ai = (text.index(marker) for marker in (ref, start, end, anchor))
        if not (core_start <= ri < core_end and down_start <= ai < si < ei < down_end):
            raise ValueError('Path markers outside their declared sections: ' + path)
        if text[ai + len(anchor):si].strip():
            raise ValueError('Anchor is not adjacent to its own canonical path: ' + path)
        # Exact canonical inner text, dropping only the marker-line delimiter.
        inner = text[si + len(start):ei]
        if inner.startswith('\n'):
            inner = inner[1:]
        if not inner.strip():
            raise ValueError('Empty canonical path: ' + path)
        blocks[path] = inner
    intervals = [(text.index('<!-- m14-path-' + p + ':start -->'),
                  text.index('<!-- m14-path-' + p + ':end -->')) for p in 'abc']
    intervals.sort()
    if any(intervals[i][1] >= intervals[i + 1][0] for i in range(2)):
        raise ValueError('Overlapping or nested canonical paths')
    for path, body in blocks.items():
        core = core.replace('<!-- m14-core-path-' + path + ' -->', body, 1)
    return '## 核心结果\n' + core.lstrip('\n'), blocks

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    raw = args.input.read_bytes()
    text = raw.decode('utf-8')
    core, blocks = project(text)
    metadata = {
        'artifact_role': 'derived_legacy_core_view_not_canonical_main',
        'contract_id': 'PATENT-SKILLS-CONTRACT-0.2.0',
        'source_filename': args.input.name,
        'source_sha256': digest(raw),
        'path_body_sha256': {p: digest(b.encode('utf-8')) for p, b in blocks.items()},
        'verification_scope': 'marker_identity_and_exact_text_projection_only'
    }
    view = '<!-- ' + json.dumps(metadata, ensure_ascii=False) + ' -->\n' + core
    # Exclusive creation also prevents overwriting the canonical input itself.
    with args.output.open('x', encoding='utf-8', newline='') as stream:
        stream.write(view)
    print(json.dumps({'output': str(args.output), 'sha256': digest(view.encode('utf-8')),
                      'source_sha256': metadata['source_sha256']}, ensure_ascii=False))

if __name__ == '__main__':
    main()
