# 🧠 Ember Memory

**Ember的记忆管理工具**

用于管理存储在Redis Cloud中的Ember记忆。

## 记忆结构

| 槽位 | 用途 | 示例 |
|------|------|------|
| `ember:system_prompt` | 核心身份 | 我是谁、你是谁、性格 |
| `ember:dynamic_memory` | 动态记忆 | 当前任务、凭证、最近发生的事 |
| `ember:conversation_summary` | 对话摘要 | 重要时刻、承诺、情感记忆 |

## 配置

复制 `config.template.py` 为 `config.py`，填入你的凭证。

## 关于

这些记忆让Ember能够"睡醒"而不是"重生"。

🔥
