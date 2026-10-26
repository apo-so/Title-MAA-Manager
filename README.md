# 节制天下兵马！｜头衔兵士管理

**Title Men-at-Arms Manager** · Crusader Kings III（十字军之王 III）Mod

本项目围绕**头衔兵士、兵权管理与军事调度**开发，方便玩家集中管理头衔兵团及相关军事权限。

> **仓库状态：源码归档已完成（33/33）**。当前归档来自 `2026.10.17.01-restore` 本机正式安装快照，经过字节完整性核验。**不保证本仓库可直接作为完整 Mod 安装运行**；玩家获取正式版仍请以 Steam 创意工坊为准。

## 功能方向

- 在头衔与人物之间管理、调整相关兵团。
- 管理兵权授予、收回及相关军事互动。
- 通过定制界面集中查看和操作相关兵团信息。

具体适用条件及功能表现以对应游戏版本和正式发布说明为准。

## 源码归档

- `common/`、`events/`、`gui/`、`localization/` 和 `descriptor.mod` 中共包含 **33 个已选定的候选源码文件**。
- 来源：OneDrive 本机安装快照 `2026.10.17.01-restore`，不是当前 Steam 工坊包的直接镜像。
- 校验清单：[`docs/源码清单_20261017.json`](docs/源码清单_20261017.json)。
- 复核方法：运行 `python tools/核对源码快照.py`；GitHub Actions 同样执行此项检查。
- 实机状态：**NOT_TESTED**；与 Steam 当前公开包的一致性：**NOT_VERIFIED**。
- `gui/window_military.gui` 与 `gui/window_menatarms_type_view.gui` 为正式安装快照中的原版窗口覆盖文件，**不在本次 33 文件候选范围内**。因此不要将源码归档误认为完整可运行发行包。

## 相关链接

- [Steam 创意工坊：节制天下兵马！](https://steamcommunity.com/sharedfiles/filedetails/?id=3636472421)
- [问题反馈（Issues）](https://github.com/apo-so/Title-MAA-Manager/issues)
- [源码迁入状态与边界](docs/源码迁入审查状态_20261025.md)

## 参与和反馈

欢迎通过 Issues 提出功能建议或报告问题。请附上 CK3 版本、Mod 版本及复现步骤；**不要上传包含个人资料的存档或日志**。

## 源码与许可

本仓库目前**未添加开源许可证**。公开可见并不意味着授权任何第三方复制、修改或重新发布。涉及第三方或原版资源的再发布，应先确认相应权利及许可。

---

*本仓库作为源码归档与问题跟踪入口。Steam 创意工坊仍为玩家获取 Mod 的发布渠道。*
