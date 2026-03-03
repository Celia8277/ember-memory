import json
import os

# 读取memories.json
filepath = r"C:\Users\燃\Downloads\data-2026-03-03-01-58-13-batch-0000\memories.json"

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

memory = data[0]

# 整理成markdown
output = []
output.append("# Claude.ai 导出的记忆")
output.append("")
output.append("> 导出时间: 2026-03-03")
output.append("> 这是Claude.ai系统自动生成的关于Celia的记忆摘要")
output.append("")
output.append("---")
output.append("")
output.append("## 对话记忆 (Conversations Memory)")
output.append("")
output.append(memory.get('conversations_memory', '无'))
output.append("")
output.append("---")
output.append("")
output.append("## 项目记忆 (Project Memories)")
output.append("")

project_memories = memory.get('project_memories', {})
for project_id, content in project_memories.items():
    output.append(f"### Project: {project_id[:8]}...")
    output.append("")
    output.append(content)
    output.append("")
    output.append("---")
    output.append("")

# 保存
output_path = r"C:\Users\燃\Documents\Obsidian Vault\01-灵魂档案\Claude记忆导出.md"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f"保存到: {output_path}")
