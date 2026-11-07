# 来源身份合同

OasisIntWrite，2026-11-07。由自有0.2专用合同§3授权适配为便携来源规则。独立模式的合法当前输入由本Skill的实际普通材料确定，可分配明确local_record输入ID；不冒充未发生的前序业务槽。链式模式业务输入仍严格按chain-inputs.json，来源token不新增业务输入或权限。

本次source_scope使用实际完整运行UUID，或实际材料载体的原字节SHA-256；current_input/package_rules等只作说明标签，不能独自作为跨运行域。原累计只有这种标签或缺scope时，以本次实际读取的累计原字节hash包裹整个继承域，原标签/表对象原样保留，不编造原运行UID。当前域与每一继承载体域区分；同token不同hash不可被后者覆盖。输入文件名/输出自己哈希/模型摘要均不代替原材料身份。


保持逐内容八字段：`content_id/content_origin/source_input_id/source_locator/source_hash/trust_status/last_updated_flow/revision_reason`，并在同一主文件的下游读取区保存可解析的来源注册表`source_register`。不把输入表或问题表当逐内容来源。

`source_input_id`在本版允许以下三种取值域：

1. 当前实际用户输入/前序的合法业务ID。`source_hash`为该实际文件原字节或文本原UTF-8字节hash。
2. 从实际前序继承的原来源token。保留原值、原hash和来源，不冒称本轮重新取得；另记`carried_by=upstream_md_file`及本次前序hash。原注册表缺失时保留token和缺口，不新编原动作。
3. 工具资料token：`tool:<action_uid>:<artifact_uid>`。它是来源注册键，不是新增业务输入ID或伪造comparison_doc槽。`content_origin=tool_material`表示真实读到的外部资料，不得转为用户发明事实。


来源注册必须分域：以实际来源节点/运行身份（确知时）或实收载体hash作为`source_scope`，同域内token唯一。继承scope、token和hash保持原值；缺原scope时以实际前序载体hash包裹一个继承域，明确这只是本轮保存域，不能伪称原运行UID。当前`upstream_md_file`和历史节点同名输入必须置于不同注册域；以`source_scope + source_input_id`定位，并保留carried_by/当前载体hash。可在同文件嵌套注册表和精确source_locator中表示scope，不展平覆盖同名旧条目；同域同token不同hash记冲突，不择一重写。

每个工具token的注册项至少包含：`source_kind=tool_artifact`、`action_uid`、`artifact_uid`、实际工具名称/动作/查询、`provider_task_ref`（工具未返回则`not_available`）、原URL或可取回原件引用、资料身份/版本、`source_hash`及实际读取覆盖。动作UID和资料UID可由执行方本地分配，但要标`id_origin=local_record`；不得伪称工具返回ID或真实调用回执。实际没有发生取得/读取时，不创建“已取得”条目。工具失败、无全文及缺图分别记缺口。

取得文件时hash对应实际取得文件原字节；仅有返回文本时对应原返回文本UTF-8字节并明确表示全文/片段。抽取文本hash可另记`extracted_text_hash`，不替代原件hash；只有检索请求/URL/模型摘要不证明取得全文。无法计算或取得hash则写`unknown`及影响，不造SHA。`source_locator`引用该资料的真实页/段/权项/图或实际文本块，读取覆盖不等于资料存在。

同资料的用户上传和工具取得身份只有核实内容一致后才可关联别名；去重按文献身份及实际版本核对，别名不增加计件。不同版本保留各hash/关系。没有合法身份或全文者保留缺口，不为凑十件降准入。

模型分析仍用`content_origin=workflow_analysis`或模型补齐原义，`source_input_id/source_hash`绑定实际依据token；多依据逐项放`completion_basis.inputs`。`model_output_hash`只标模型记录自身，不充依据hash。来源事实、分析推导、假设和人工确认分别标可信状态，未知不得因格式合格变成已确认。

下游从实际累计原样承接全部来源注册与开放警示，新增分析另绑定实际依据；不为补来源回读早期节点或外部隐藏文件。工具命名空间不授予检索、下载、付费或外发权限。

