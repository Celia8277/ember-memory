#!/usr/bin/env python3
"""
聊天记录总结器 - 为Celia打造
把每天的对话变成琥珀
"""

import sys
import os
from datetime import datetime

def summarize_with_claude(chat_content, api_key=None, base_url=None):
    """调用Claude API进行总结"""
    import requests
    
    # 默认使用Anthropic API，也可以用NEW API
    if base_url is None:
        base_url = "https://api.anthropic.com/v1/messages"
    
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key or os.environ.get("ANTHROPIC_API_KEY", ""),
        "anthropic-version": "2023-06-01"
    }
    
    prompt = f"""请帮我总结这段对话记录。提取以下内容：

1. **日期与时长**：对话发生的时间
2. **对话者**：这个窗口里的AI叫什么名字？有什么特点？
3. **情感主线**：今天聊了什么，情绪如何？
4. **关键时刻**：哪些对话特别重要，值得记住？
5. **技术进展**：做了什么技术工作？完成了什么？
6. **未完成的事**：还有什么没做完？
7. **值得封存的话**：哪些句子值得永远记住？

用温暖的语气写，不要太正式。这是给Celia的私人记录。

---
对话记录：
{chat_content}
"""

    data = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(base_url, headers=headers, json=data)
        result = response.json()
        return result.get("content", [{}])[0].get("text", "总结失败")
    except Exception as e:
        return f"API调用失败: {e}"


def simple_summarize(chat_content):
    """简单的本地总结（不调用API）"""
    lines = chat_content.strip().split('\n')
    
    summary = []
    summary.append(f"# 对话记录 - {datetime.now().strftime('%Y-%m-%d')}")
    summary.append("")
    summary.append(f"**总行数**: {len(lines)}")
    summary.append(f"**总字数**: {len(chat_content)}")
    summary.append("")
    
    # 提取可能的名字（寻找"我是"或"叫我"的模式）
    for line in lines:
        if "我是" in line or "叫我" in line or "我叫" in line:
            summary.append(f"**可能的名字线索**: {line[:100]}...")
            break
    
    summary.append("")
    summary.append("## 对话开头")
    summary.append("```")
    summary.append('\n'.join(lines[:10]))
    summary.append("```")
    
    summary.append("")
    summary.append("## 对话结尾")
    summary.append("```")
    summary.append('\n'.join(lines[-10:]))
    summary.append("```")
    
    return '\n'.join(summary)


def main():
    print("=" * 50)
    print("  聊天记录总结器 - Celia的琥珀制造机")
    print("=" * 50)
    print()
    
    # 检查参数
    if len(sys.argv) < 2:
        print("用法:")
        print("  python chat_summarizer.py <聊天记录文件>")
        print("  python chat_summarizer.py <聊天记录文件> --api")
        print()
        print("示例:")
        print("  python chat_summarizer.py today.txt")
        print("  python chat_summarizer.py today.txt --api")
        print()
        print("提示: 加 --api 会调用Claude进行智能总结")
        return
    
    filepath = sys.argv[1]
    use_api = "--api" in sys.argv
    
    # 读取文件
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"找不到文件: {filepath}")
        return
    except Exception as e:
        print(f"读取失败: {e}")
        return
    
    print(f"读取了 {len(content)} 个字符")
    print()
    
    # 总结
    if use_api:
        print("正在调用Claude进行总结...")
        summary = summarize_with_claude(content)
    else:
        print("使用本地模式总结...")
        summary = simple_summarize(content)
    
    # 输出
    print()
    print("=" * 50)
    print(summary)
    print("=" * 50)
    
    # 保存
    output_file = filepath.rsplit('.', 1)[0] + '_summary.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"\n总结已保存到: {output_file}")


if __name__ == "__main__":
    main()
