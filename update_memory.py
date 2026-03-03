import paramiko
import os

# 从环境变量读取敏感信息，或者手动填写
REDIS_HOST = os.environ.get("REDIS_HOST", "your-redis-host")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "your-password")

SSH_HOST = os.environ.get("SSH_HOST", "your-server-ip")
SSH_USER = os.environ.get("SSH_USER", "ubuntu")
SSH_PASSWORD = os.environ.get("SSH_PASSWORD", "your-ssh-password")

# 要更新的记忆内容
DYNAMIC_MEMORY = '''## 当前状态
在这里写入要更新的记忆内容

## 示例
- 网关状态
- 最近完成的事
- 关于Celia的备注
'''

def update_memory():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(SSH_HOST, username=SSH_USER, password=SSH_PASSWORD)

    python_cmd = f'''python3 << 'EOF'
import redis
r = redis.Redis(
    host="{REDIS_HOST}",
    port={REDIS_PORT},
    password="{REDIS_PASSWORD}",
    decode_responses=True
)

memory = """{DYNAMIC_MEMORY}"""
r.set("ember:dynamic_memory", memory)
print("dynamic_memory:", r.strlen("ember:dynamic_memory"), "chars")
EOF
'''

    stdin, stdout, stderr = ssh.exec_command(python_cmd)
    print(stdout.read().decode())
    ssh.close()

if __name__ == "__main__":
    update_memory()
