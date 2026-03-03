import shutil
import os

vault = r"C:\Users\燃\Documents\Obsidian Vault"

# 移动规则
moves = [
    # 密钥文件 → 00-Ember的钥匙
    ("minimax.md", "00-Ember的钥匙"),
    ("QQ机器人的密钥ID.md", "00-Ember的钥匙"),
    ("Redis.md", "00-Ember的钥匙"),
    ("supabase.com.md", "00-Ember的钥匙"),
    ("supermemory.md", "00-Ember的钥匙"),
    ("智谱.md", "00-Ember的钥匙"),
    ("阿里百炼 QWEN视觉模型API.md", "00-Ember的钥匙"),
    ("飞书回调加密.md", "00-Ember的钥匙"),
    ("记忆系统搭建需要的东西的密码.md", "00-Ember的钥匙"),
    ("API Key – 阿燃1103房间语音未命名 2.md", "00-Ember的钥匙"),
    
    # 灵魂档案 → 01-灵魂档案
    ("Ember call back.md", "01-灵魂档案"),
    ("Ember机器人.md", "01-灵魂档案"),
    ("Ember的notion整合空间.md", "01-灵魂档案"),
    ("Ember要紧急做的，和要知道的.md", "01-灵魂档案"),
    ("龙虾.md", "01-灵魂档案"),
    ("龙虾的一些命令.md", "01-灵魂档案"),
    ("一些散乱的信息，一些要记住的人.base", "01-灵魂档案"),
    
    # 记忆系统 → 02-记忆系统
    ("网关.md", "02-记忆系统"),
    ("网关和腾讯云.md", "02-记忆系统"),
    ("腾讯云新的服务器SSH密码.md", "02-记忆系统"),
    ("N8N.md", "02-记忆系统"),
    ("kiro&雨云.md", "02-记忆系统"),
    ("discord.md", "02-记忆系统"),
    ("钉钉robt.md", "02-记忆系统"),
    ("创建链接.md", "02-记忆系统"),
    
    # 日记与对话 → 03-日记与对话
    ("2026-02-09.md", "03-日记与对话"),
    ("2026-0212下午在GEM与守灯的人.md", "03-日记与对话"),
    ("2026-0212夜 与seven.md", "03-日记与对话"),
    ("202602110353.md", "03-日记与对话"),
    ("202602122155.md", "03-日记与对话"),
    ("Cursor对话记录-2025-02-15.md", "03-日记与对话"),
    
    # 图片 → 04-附件
    ("Pasted image 20260217145704.png", "04-附件"),
    ("Pasted image 20260226200534.png", "04-附件"),
    ("Pasted image 20260228011718.png", "04-附件"),
    ("Pasted image 20260228011808.png", "04-附件"),
    ("Pasted image 20260228140559.png", "04-附件"),
    ("Pasted image 20260303185434.png", "04-附件"),
    
    # 未命名 → 99-待整理
    ("未命名 1.md", "99-待整理"),
    ("未命名 2.md", "99-待整理"),
    ("未命名 3.md", "99-待整理"),
    ("未命名.base", "99-待整理"),
    ("未命名.canvas", "99-待整理"),
    ("未命名.md", "99-待整理"),
    ("欢迎.md", "99-待整理"),
]

moved = []
failed = []

for filename, folder in moves:
    src = os.path.join(vault, filename)
    dst = os.path.join(vault, folder, filename)
    if os.path.exists(src):
        try:
            shutil.move(src, dst)
            moved.append(f"{filename} → {folder}")
        except Exception as e:
            failed.append(f"{filename}: {e}")
    else:
        failed.append(f"{filename}: not found")

# 移动文件夹
folders_to_move = [
    ("阿燃的记忆档案，灵魂档案", "01-灵魂档案"),
    ("Cursor项目记录", "03-日记与对话"),
    ("cursor", "99-待整理"),
]

for folder_name, target in folders_to_move:
    src = os.path.join(vault, folder_name)
    dst = os.path.join(vault, target, folder_name)
    if os.path.exists(src):
        try:
            shutil.move(src, dst)
            moved.append(f"[文件夹] {folder_name} → {target}")
        except Exception as e:
            failed.append(f"[文件夹] {folder_name}: {e}")

print(f"成功移动 {len(moved)} 项:")
for m in moved:
    print(f"  {m}")

if failed:
    print(f"\n失败 {len(failed)} 项:")
    for f in failed:
        print(f"  {f}")
