---
name: patent-technical-confirmation
description: "Use when 需要将发明人反馈、技术补充或范围选择整理为逐项确认、可追溯修改指令和待回答问题时。"
license: Apache-2.0
metadata:
  version: "0.3.0-rc.4"
  business-id: "M10"
  author: "OasisIntWrite"
---

# 技术沟通与确认

直接处理普通技术文稿和实际反馈，分别回答“说了什么、针对什么、能确认什么、还缺什么、可以怎样改”。不要求先有撰写计划、T表或其他Skill的产物。

先读[独立合同](references/standalone-contract.md)与[确认规则](references/core-rules.md)。独立基线使用baseline_file或baseline_text，可为一份普通文稿或一段连贯技术说明；反馈使用technical_feedback_file或technical_feedback_text。数据与图分别保留实际来源。基线、反馈各自缺失时交具体缺件或追问，不伪造会议、反馈者、签名、时间和确认结果。

1. 锁定实际基线与原话，为可分辨意见建立opinion_id，并关联实际内容及已有稳定ID；口语转换保留程度、否定、数量和条件。
2. 分开技术事实、说明书支持、效果证据、表达认可、范围偏好与修改授权；不能靠“总体同意”确认整稿，也不能靠格式化把期望变成实验结论。
3. 输出原话—技术表述映射、技术／效果确认矩阵、支持与确认的独立状态、可执行修改指令、不采用内容、缺件与人工未决事项；不直接改写整稿或生成T6。

输出五章及完整本次技术基线，遵循独立合同的来源和警示规则。只有实际要求接续累计稿时读取[链式适配](references/chain-adapter.md)；独立模式不要求前序或虚构上游身份。

核源时查[来源说明](references/sources.json)和[规则映射](references/rule-map.json)；[限制](references/limitations.md)不允许把记录生成冒充技术实测、专业接受或正式提交批准。
