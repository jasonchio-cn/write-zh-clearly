# 中文表达优化

围绕接收者当前需要，优化中文答复和文档的内容取舍、信息组织和语言表达，保留原有事实、条件和要求，让读者更容易理解、判断和行动。

版本更新见 [CHANGELOG.md](CHANGELOG.md)。

插件提供 `write-zh-clearly` Skill，适用于 Codex 和 Qoder CLI。生成或修订面向人阅读的中文答复和文档后，Agent 可以在交付前使用它检查表达；用户提出精简、重组或润色等要求时也可以使用。

本插件尚未适配 Claude Code。

## 安装

选择使用的客户端，添加 GitHub 仓库中的插件市场并安装：

```bash
# Codex
codex plugin marketplace add jasonchio-cn/write-zh-clearly
codex plugin add write-zh-clearly@write-zh-clearly

# Qoder CLI
qodercli plugins marketplace add https://github.com/jasonchio-cn/write-zh-clearly.git
qodercli plugins install write-zh-clearly@write-zh-clearly
```

Qoder 安装后重启 CLI 或运行 `/plugins reload`。如果已通过其他方式安装同名 Skill，请检查已有部署，避免重复加载。

更新插件：

```bash
# Codex
codex plugin marketplace upgrade write-zh-clearly
codex plugin add write-zh-clearly@write-zh-clearly

# Qoder CLI
qodercli plugins marketplace update write-zh-clearly
qodercli plugins update write-zh-clearly@write-zh-clearly
```

## 使用

可以在概念或仓库介绍、技术方案讨论、OpenSpec 产物、日报周报、内容总结，以及需要读者知晓或决策的说明中使用。Skill 根据接收者已有信息和本次用途，提炼主旨、讲清关系，必要时用具体例子解释难点，并删除无实际作用的铺垫与反复澄清。

独立改稿时，提供原文和需求，例如：“帮我把这段说明写得更清楚，保留所有条件和限制。”Skill 默认交付完整改稿；如需解释修改，可以在请求中说明。

作为其他任务的交付前检查时，修改直接落实到原回复或产物，并沿用原任务的校验和交付约定。例如，生成 OpenSpec 文件时检查文件中的中文表达，并按原任务约定反馈结果。

## 许可证

[MIT License](LICENSE)
