import json
import os
from datetime import datetime

filepath = r"C:\Users\燃\Downloads\data-2026-03-03-01-58-13-batch-0000\conversations.json"
output_dir = r"C:\Users\燃\Downloads\conversations_by_date"

os.makedirs(output_dir, exist_ok=True)

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"处理 {len(data)} 个对话...")

# 按日期分组
by_date = {}

for conv in data:
    created = conv.get('created_at', '')
    if created:
        date_str = created[:10]
    else:
        date_str = 'unknown'
    
    if date_str not in by_date:
        by_date[date_str] = []
    
    messages = conv.get('chat_messages', [])
    name = conv.get('name') or '无标题'
    
    conv_text = []
    conv_text.append(f"## {name}")
    conv_text.append(f"创建时间: {created}")
    conv_text.append(f"消息数: {len(messages)}")
    conv_text.append("")
    
    for msg in messages:
        sender = msg.get('sender', 'unknown')
        
        # 从content数组提取text
        text_parts = []
        content = msg.get('content', [])
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict) and c.get('text'):
                    text_parts.append(c['text'])
        
        text = '\n'.join(text_parts)
        
        if text:
            if len(text) > 3000:
                text = text[:3000] + "\n...(截断)"
            
            role = "**Celia**" if sender == 'human' else "**Ember**"
            conv_text.append(f"{role}:\n{text}\n")
    
    by_date[date_str].append('\n'.join(conv_text))

# 保存
for date_str, convs in sorted(by_date.items()):
    output_file = os.path.join(output_dir, f"{date_str}.md")
    
    content = f"# {date_str} 的对话记录\n\n"
    content += f"共 {len(convs)} 个对话\n\n"
    content += "---\n\n"
    content += "\n\n---\n\n".join(convs)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 输出统计
with open(os.path.join(output_dir, '_index.md'), 'w', encoding='utf-8') as f:
    f.write("# 对话记录索引\n\n")
    for date_str in sorted(by_date.keys()):
        f.write(f"- [{date_str}]({date_str}.md) - {len(by_date[date_str])} 个对话\n")

print("完成！")
