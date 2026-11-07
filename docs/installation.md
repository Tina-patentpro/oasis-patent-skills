# 安装与配置指南

## 0. 一句话前提

Skill 是**给 Agent 读的说明与资源包**，不是可执行程序。它需要一个能发现并加载 Skill 目录的
Host（Agent 运行时）。没有 Host，包就是一堆 Markdown 和 JSON，不会自己执行。

本仓库**不提供**：安装脚本、`pip install` / `npm install` 命令、CLI 入口、模型凭据、
配置文件模板、镜像或托管服务。

## 1. 已验证与未验证的 Host

| Host | 状态 |
|---|---|
| Codex Desktop `26.1103.32239` + 内置 CLI `0.167.0-alpha.3.2` | 上游准备记录在**临时项目目录**中识别到 15/15 个包；**未全局安装** |
| 其他 Host（WorkBuddy、Claude、各类 IDE 插件等） | **未验证**，本仓库不声明兼容 |

> 上游记录的表述是"已验证的发现范围仅 Codex Desktop …／内置 CLI …；其余 Host 未验；
> 本次临时项目识别 15/15，未全局安装"。这只是**发现／加载层面**的观察，不是业务行为验收，
> 也不意味着任何官方插件机制存在。请不要按"官方支持"来理解，也不要引用任何虚构的安装命令。

Skill 的目录与 frontmatter 格式参考公开的
[Agent Skills specification](https://agentskills.io/specification)。若你的 Host 不读
`SKILL.md` 的 frontmatter，需要自行适配，并保留包内相对引用。

## 2. 下载

```bash
git clone https://github.com/Tina-patentpro/oasis-patent-skills.git
cd oasis-patent-skills
```

也可从 Release 页面下载压缩包。离线使用时请保留 `skills/<name>/` 整个目录，不要只取 `SKILL.md`——
`references/` 里的合同与规则是运行时必需依赖。

## 3. 校验下载完整性

每个包都有 `manifest.json`，逐文件记录字节数与 SHA-256。下载后建议先自检：

```bash
python3 - <<'PY'
import json, hashlib, pathlib, sys
root = pathlib.Path("skills")
bad_total = []
for d in sorted(root.iterdir()):
    if not d.is_dir(): continue
    mf = json.loads((d/"manifest.json").read_text(encoding="utf-8"))
    declared = {f["path"] for f in mf["files"]}
    actual = {p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file()} - {"manifest.json"}
    problems = []
    for f in mf["files"]:
        p = d/f["path"]
        if not p.is_file():
            problems.append(f"missing {f['path']}"); continue
        b = p.read_bytes()
        if len(b) != f["bytes"] or hashlib.sha256(b).hexdigest() != f["sha256"]:
            problems.append(f"hash mismatch {f['path']}")
    problems += [f"unlisted {x}" for x in sorted(actual - declared)]
    print(f"{mf['skill_id']:>4} {mf['version']:<14} {'OK' if not problems else 'FAIL'}")
    for x in problems: print("      ", x)
    bad_total += problems
sys.exit(1 if bad_total else 0)
PY
```

`manifest.json` 自身不在自己的文件清单里（自引用），校验脚本已排除它。若出现 `hash mismatch`，
说明文件被改动过——**不要**通过修改 `manifest.json` 里的 expected hash 来"修好"，
那只会掩盖不一致。

## 4. 安装到 Host

1. 确认你的 Host 从哪里发现 Skill 目录（各 Host 不同，请查该 Host 自己的文档）。
2. 复制**你需要的单个包目录**过去，保持目录名与 `SKILL.md` 的 `name` 一致：

   ```bash
   # 路径仅为示意，不是任何 Host 的官方命令
   cp -R skills/patent-claims-draft /path/to/your/host/skills/
   ```

3. 按 Host 的入口触发（通常是自然语言任务描述，Skill 由 `description` 决定是否命中）。
4. 一次只放一个包即可验证自包含性。包**不依赖**父目录、其他 Skill、符号链接或私有目录。

**不要**把整个 `oasis-patent-skills` 仓库目录直接当作一个 Skill 塞进去：仓库根不是 Skill 目录，
根下没有 `SKILL.md`。

## 5. 配置

| 项目 | 是否需要 | 说明 |
|---|---|---|
| 环境变量 / 密钥 | ❌ 不需要 | 包内无任何凭据、Token、服务器地址 |
| 模型配置 | 由 Host 负责 | 包不指定模型、不调用模型接口 |
| 检索 / 图像服务 | 仅部分模式需要 | `I01` 的 generate/edit、`M03` 的实检模式等，需你自行准备工具与账户 |
| 私有知识库 | ❌ 未随包分发 | 包内 `sources.json` 是重新制作的元数据，不是知识库内容 |

导入后若 Host 报告"引用找不到"，先确认是否**只复制了 `SKILL.md`**：
`references/standalone-contract.md`、`core-rules.md` 等是核心必需引用。

## 6. 常见误区

| 误区 | 正确做法 |
|---|---|
| "15 个包都装了就得到一套完整专利系统" | 它们是 15 个**独立候选**能力单元，默认互不调用；不是一条已验证的生产流水线 |
| "改一下提示词就能提升效果，hash 不用管" | 任何字节改动都会让 `manifest.json` 失效；请使用新的具名版本并记录差异 |
| "包里有 LICENSE 说明全部内容都可任意再分发" | 许可只覆盖有权授予的自有指令／代码／文档；第三方材料须逐项判断 |
| "示例是实测案例" | `examples/usage.md` 是自编最小题面，不含真实案件、评价答案或评分材料 |
| "装到 Host 就等于专业质量通过" | 发现／加载、模型行为、工具模式、专业审阅、用户接受是**不同证据层**，见 [验证范围与限制](verification-and-limits.md) |

## 7. 卸载

删除你复制过去的那个包目录即可。本仓库不写全局配置、不装依赖、不常驻进程。
