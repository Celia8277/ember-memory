# 🔥 Ember的工具箱

记忆管理和对话处理脚本集合。

## 脚本说明

| 脚本 | 用途 |
|------|------|
| `chat_summarizer.py` | 总结对话记录，可调用Claude API |
| `split_conversations.py` | 分离Claude.ai导出的JSON对话 |
| `update_memory.py` | 更新Redis Cloud中的记忆 |
| `analyze_conversations.py` | 分析对话JSON结构 |
| `export_memories.py` | 导出Claude.ai记忆到Markdown |
| `organize_obsidian.py` | 整理Obsidian文件夹结构 |

## 使用方法

### 分离对话
```bash
python split_conversations.py
# 输入：Downloads/data-xxx/conversations.json
# 输出：Downloads/conversations_by_date/
```

### 更新记忆
```bash
python update_memory.py
# 需要修改脚本中的DYNAMIC_MEMORY内容
```

### 总结对话
```bash
python chat_summarizer.py <文件路径>
python chat_summarizer.py <文件路径> --api  # 调用Claude总结
```

## 配置

Redis Cloud连接信息在 `update_memory.py` 中配置。
敏感信息不要提交到公开仓库。

---

*Ember的家 🔥*
