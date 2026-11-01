# 中文表达优化

优化中文内容的取舍、组织和语言表达，保留原文的事实、条件和要求，让读者更容易理解和行动。

版本更新见 [CHANGELOG.md](CHANGELOG.md)。

插件提供 `write-zh-clearly` Skill，适用于 Codex 和 Qoder CLI。生成或修订面向人阅读的中文成稿后，Agent 可以在交付前使用它检查表达；用户提出精简、重组或润色等要求时也可以使用。

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

直接提出需求并提供原文，例如：“帮我把这段说明写得更清楚，保留所有条件和限制。”

Skill 默认交付完整改稿；如需解释修改，可以在请求中说明。

## 许可证

[MIT License](LICENSE)
