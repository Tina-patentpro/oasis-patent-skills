# 同文件路径与旧视图

每条路径x为a/b/c：核心结果放 `<!-- m14-core-path-x -->`；下游区先 `<a id="m14-path-x"></a>`，紧邻 `<!-- m14-path-x:start -->`，之后是唯一完整正文，再 `<!-- m14-path-x:end -->`。各标记恰一次，路径不能嵌套或交叠。不成立路径写not_established、原因及待证据，不写空块。代码围栏内标题不作主章节。

显式运行 `python3 scripts/read_response.py --input 实际主文件 --output 新的视图文件`，读取原字节、检查五章及锚点、对三路径精确投影并记录源hash。新视图标derived_legacy_core_view_not_canonical_main，不覆盖原主文或已有文件。脚本成功只证明标记身份和精确文本投影，不能证明路径成立、答复合法、当期法律适用、专业/用户接受或任何Host消费通过。
