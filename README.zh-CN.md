# Xiaohongshu Content Workflow
# 小红书内容运营工作流

把账号目标、资料研究、选题、图文与短视频制作、发布后复盘、偏好学习连接成一个项目。面向个人创作者和小团队，可由一个 Agent 连续执行，也可按任务分工。

这是从长期内容协作中重写、脱敏的 **7 个 Agent Skills + 项目 Workflow + 专项 SOP**。保留改稿、判断、交接和复盘中容易出错的细节；不预置作者的个人语气、领域身份、发布配比或工具账号。

[English](README.md) · [项目工作流](docs/WORKFLOW.md) · [兼容性](docs/COMPATIBILITY.md) · [验证状态](docs/VALIDATION.md)

## 包含什么
| Skill | 何时调用 | 交付 |
|---|---|---|
| [xhs-content-ops](skills/xhs-content-ops/SKILL.md) | 开始或恢复账号项目、运行完整内容闭环、协调任务 | 账号简表、当前任务、状态和接续 |
| [xhs-source-research](skills/xhs-source-research/SKILL.md) | 分析官方/竞品材料、评论、核查内容依据 | 来源记录、可用判断、迁移条件 |
| [xhs-topic-planning](skills/xhs-topic-planning/SKILL.md) | 选题取舍、周计划、把灵感变为框架 | 内容简报、创作契约、可执行排期 |
| [xhs-post-writing](skills/xhs-post-writing/SKILL.md) | 标题、封面、卡片、正文、修改和发布准备 | 图文发布包或指定组件 |
| [xhs-video-production](skills/xhs-video-production/SKILL.md) | 已有方向需要短视频脚本、分镜和制作交接 | 素材表、时间线、提示词、发布文案 |
| [xhs-performance-review](skills/xhs-performance-review/SKILL.md) | 单篇/周复盘、数据与评论解释、归档 | 可支持的结论、下一轮动作、版本化记录 |
| [xhs-preference-learning](skills/xhs-preference-learning/SKILL.md) | 从改稿、终稿和纠正中记录自己的偏好 | 有范围、来源、反例、状态的个人偏好记录 |

## 保留下来的执行细节
- 长说明先还原动机、担心、正向目标和认可样本，不压成“写得自然一点”。
- 选题区分读者当下问题、账号持续问题、材料条件与制作成本，不为了排满一周强行生产。
- 图文卡承担论证和注意力结构；正文可补条件、实例和作者判断，避免机械复述。
- 区分局部改稿、全局表达调整、事实变化；精确回滚认可稿，更新受新事实影响的结论。
- 分开实际发布版本与助手草稿，检查指标分母和窗口，评论原文缺失时不猜评论内容。
- 偏好有适用范围和失效条件，单篇纠正不会自动成为所有内容的禁令。
- 数据和工具暂不可得时交付可完成部分，明确余下依赖，不伪造自动发布、采集或长期记忆。

## 安装
使用 Python 3.10+；核心 Skills 本身不依赖 Python，脚本只用于复制和检查。

在本仓库根目录执行，先预览将写入的位置：
```sh
python scripts/install.py --agent codex --project /path/to/your/content-project
```
确认路径后加 `--apply`。Claude Code 使用 `--agent claude-code`，Cursor 使用 `--agent cursor`。也可以用 `--skill xhs-post-writing` 只安装一个模块。每个模块的必要参考与模板均在自己的目录中，单独复制也能使用。

安装器不联网、不修改凭据、不覆盖已有目录；更新时先比较旧副本与新副本。宿主重新发现技能的方式见其当前文档。纯聊天环境可读取相关指令，但不因此获得文件持久化或平台操作能力。

## 使用
直接提出实际任务，例如：
- “帮我规划小红书这周的内容。我只有周末能拍摄，已有三条未发布素材。”
- “只改这篇的正文，保留我确认的卡片和标题。”
- “结合这些发布截图、数据和评论做复盘，告诉我下条具体改什么。”
- “以后这类测评保留专业术语，但解释清楚。这是我认可的终稿，请记录这个偏好。”

完整项目由 `xhs-content-ops` 接续；单一任务直接调用对应 Skill。无须先填写全部模板。

## 能力与边界
文件输入即可完成主要策划、写作和复盘。联网研究、媒体生成、平台发布、数据采集由宿主实际工具提供，包内没有隐藏爬虫、自动发帖或定时任务。支持范围按宿主与任务核验，不承诺“所有模型通用”或增长效果。

个人运行资料默认放在使用者项目的 `.xhs-work/`，与公开技能分开；若自己的项目会上传 GitHub，也要将该目录加入自己的忽略规则。不要上传原始私聊、个人偏好库、账号数据或含身份的截图。

## 维护
```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```
结构检查不等于内容效果。行为测试、实际检查范围和未验证项见 [验证状态](docs/VALIDATION.md)。贡献方法时请提供真实问题、可公开输入、预期行为及适用边界，见 [贡献说明](CONTRIBUTING.md)。

版本 0.1.0 · MIT · [来源与改写原则](docs/SOURCES.md)
