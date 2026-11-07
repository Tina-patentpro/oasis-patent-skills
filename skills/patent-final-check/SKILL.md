---
name: patent-final-check
description: "Use when 需要审阅现有权利要求、说明书、摘要和附图，核对技术支持、术语与图文一致性，或提出有证据的审查质疑时。"
license: Apache-2.0
metadata:
  version: "0.3.0-rc.4"
  business-id: "M13"
  author: "OasisIntWrite"
---

# 申请文本检查

直接检查用户提供的普通申请文稿，不要求先运行其他Skill或提供T5／T6。先读[独立合同](references/standalone-contract.md)与[检查规则](references/core-rules.md)。

完整检查使用当前权项、说明书／摘要及被引用附图；只有部分材料仍可检查实际可核部分，明确其余未评估。真实现有技术缺失时不作完整新颖性／创造性结论，也不因没有T5停止其他检查。

1. 锁定实际文本版本及任务范围，按每项独权和真实从属父链核问题、必要关系、实施路径与支持。
2. 分别核公开／支持／概括／效果、引用与单一性、术语单位、图号标记及无依据新增；区分确认状态和支持判断。
3. 每项问题交定位、原文证据、技术影响、严重程度、具体纠正／取证动作、待确认状态和使用建议。问题与模拟审查质疑相互关联，不用分数代替证据。
4. 保留全部有效正文、来源和开放警示；检查本身不取得改稿权限。关键缺口仍输出完整问题报告，不能标整体通过或直接提交就绪。

输出五章与完整本次结果；仅在实际接续累计稿时读取[链式适配](references/chain-adapter.md)。来源与规则核对见[来源说明](references/sources.json)、[采用映射](references/rule-map.json)；适用边界见[限制](references/limitations.md)。
