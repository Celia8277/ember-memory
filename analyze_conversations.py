import json
import os
from datetime import datetime

# 读取conversations.json
filepath = r"C:\Users\燃\Downloads\data-2026-03-03-01-58-13-batch-0000\conversations.json"

# 获取文件大小
size_mb = os.path.getsize(filepath) / (1024 * 1024)
print(f"文件大小: {size_mb:.2f} MB")

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"对话数量: {len(data)}")
print()

# 看看结构
if data:
    first = data[0]
    print("对话字段:", list(first.keys()))
    print()
    
    # 按日期统计
    dates = {}
    for conv in data:
        # 尝试找日期字段
        created = conv.get('created_at') or conv.get('create_time') or conv.get('updated_at')
        if created:
            # 解析日期
            if isinstance(created, str):
                try:
                    dt = datetime.fromisoformat(created.replace('Z', '+00:00'))
                    date_str = dt.strftime('%Y-%m-%d')
                except:
                    date_str = created[:10]
            else:
                date_str = str(created)[:10]
            
            dates[date_str] = dates.get(date_str, 0) + 1
    
    print("按日期统计:")
    for date in sorted(dates.keys()):
        print(f"  {date}: {dates[date]} 个对话")
    
    print()
    print("第一个对话示例:")
    print(f"  名称: {first.get('name') or first.get('title') or '无'}")
    print(f"  创建: {first.get('created_at') or first.get('create_time') or '无'}")
    
    # 看看有没有messages字段
    if 'chat_messages' in first:
        print(f"  消息数: {len(first['chat_messages'])}")
    elif 'messages' in first:
        print(f"  消息数: {len(first['messages'])}")
