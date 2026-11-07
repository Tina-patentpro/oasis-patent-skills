# 专利制图结果与工具状态合同 V0.2.1

生成和编辑共用本合同。以下记录由执行者在已有任务记录或调用返回中整理，不要求用户填表，也不新增外部API协议。

## 字段

| 字段 | 允许值或内容 |
|---|---|
| `mode` | `generate`、`edit` |
| `status` | `generated`、`generated_with_concerns`、`edited`、`edited_with_concerns`、`prompt_ready_tool_unavailable`、`edit_plan_ready_tool_unavailable`、`needs_reference_image`、`needs_clarification`、`pending_verification`、`failed` |
| `tool_status` | `not_invoked`、`pending`、`succeeded`、`failed`、`unknown`；仅按实际工具证据填写 |
| `tool_task_ref` | 工具实际返回的任务/结果ID或资源引用；未返回写`not_available`，保留已有调用记录，不编造任务ID或查询接口 |
| `artifact_status` | `available`（实际可读取）、`unavailable`（已返回但不可访问）、`not_returned`、`not_applicable` |
| `verification_action` | 核验原任务或产物的具体下一动作；没有可用查询能力时明确待核，不以重新生成替代核验 |
| `images` | 实际产物引用；未取得可访问产物时不冒称图片已交付 |
| `checked_requirements` / `unverified_or_conflicting` | 已核与未核的数量、关系、视图、保真、文字及冲突 |

每张图分别记录这些字段。规划就绪、工具执行结果、产物可访问及图面核验分别成立，不能用单一成功标记相互替代。

## 结果分流

| 实际证据 | `status` | `tool_status` | `artifact_status` | 后续动作 |
|---|---|---|---|---|
| 工具明确报告已失败 | `failed` | `failed` | 按实际有无产物填写 | 记录错误及原任务身份；是否重试按本次授权与已确认结果决定 |
| 调用超时、响应丢失或无法确定原任务结果 | `pending_verification` | `unknown` | `not_returned`或实际已知状态 | 保留原任务/调用身份，先查原任务或等待人工核验，禁止自动重发 |
| 工具明确返回尚在执行 | `pending_verification` | `pending` | 按实际填写 | 只沿真实工具支持的方法核原任务，不预称完成或创建替代任务 |
| 工具成功，但返回文件/链接实际不可访问 | `pending_verification` | `succeeded` | `unavailable` | 核验同一产物的取回/访问，不重新出图或改图 |
| 工具成功且产物可读取，图面核验完成或有偏差 | 对应`generated/edited`或`*_with_concerns` | `succeeded` | `available` | 展示真实产物及已核/未核项，保留原图和结果身份 |
| 无工具或只交规划，未发起调用 | `prompt_ready_tool_unavailable`或`edit_plan_ready_tool_unavailable` | `not_invoked` | `not_applicable` | 交提示词或编辑合同，不冒称已生成/编辑 |
| 缺目标图或关键语义待澄清，未调用 | `needs_reference_image`或`needs_clarification` | `not_invoked` | `not_applicable` | 请求最小缺件或澄清，保留已有规划 |

未知结果不转换为已确认失败，也不因没有图片引用认定服务未执行。核到新证据后记录状态变更及依据，保留原未知记录，不回写成从未发生过未知。
