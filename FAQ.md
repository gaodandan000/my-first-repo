# 常见问题解答 (FAQ)

## ❌ `glm coding --init` 命令不存在

### 问题
运行 `glm coding --init` 时出错：
```
🚀 执行命令: coding --init
/root/.local/bin/glm: line 34: exec: coding: not found
```

### 原因
**`glm coding --init` 不是有效的命令**。这个命令来自于对几个不同工具的混淆：

1. **官方 glm CLI 工具** (xqsit94/glm)
   - 这是一个独立的工具，可以执行 `glm coding --init`
   - ⚠️ 由于网络限制，我们无法安装这个工具

2. **我们的 glm 脚本** (glm-start.sh)
   - 这是一个**环境变量加载器**，用于运行其他命令
   - 功能：`glm <command>` = 加载 .env + 运行 command
   - 不支持 `glm coding --init` 这样的子命令

3. **coding-helper** (chelper)
   - 这是智谱AI的官方配置工具
   - 正确命令：`chelper init`（不是 `glm coding --init`）

### ✅ 正确的解决方案

#### 方案1: 使用 chelper（推荐用于配置）
```bash
chelper init                 # 初始化向导（需要网络）
chelper lang set zh_CN       # 设置中文（已完成）
chelper auth glm_coding_plan_china "你的密钥"  # 配置密钥
chelper doctor               # 健康检查
```

**注意**：chelper 命令需要网络连接进行验证。

#### 方案2: 使用我们的 glm 脚本（推荐用于开发）
```bash
# 运行 Python 脚本（自动加载 API 密钥）
glm python test_glm.py

# 运行 Node.js 脚本
glm node test_glm.js

# 启动交互式 shell
glm

# 运行任何需要环境变量的命令
glm <your-command>
```

#### 方案3: 直接加载环境变量
```bash
source .env
python test_glm.py
node test_glm.js
```

---

## 🤔 其他常见问题

### Q1: 为什么我的 API 连接失败？
```
❌ 连接失败: Connection error.
```

**A**: 这是由于当前环境的网络限制导致的，无法连接到智谱AI的服务器。

**解决方案**：
- 在可以访问网络的环境中运行
- 环境变量配置是正确的，脚本在正常网络环境下会工作

---

### Q2: chelper auth 提示网络错误怎么办？
```
✖ Network error, please check your connection
```

**A**: chelper 需要网络连接来验证 API 密钥。

**解决方案**：
- 使用我们的 `glm` 脚本（不需要网络验证）
- .env 文件已经包含正确的 API 密钥
- 直接使用 `glm python script.py` 即可

---

### Q3: 如何确认环境变量已加载？
**A**: 运行测试脚本：
```bash
glm python test_glm.py
```

你会看到：
```
✅ 环境变量已加载：
   ANTHROPIC_API_KEY: ce114ad8a32c9b27af61...
   ANTHROPIC_API_BASE: https://open.bigmodel.cn/api/paas/v4
```

---

### Q4: glm 命令在哪里定义？
**A**:
- 符号链接：`/root/.local/bin/glm` → `/home/user/my-first-repo/glm-start.sh`
- Bash 别名：`~/.bashrc` 中定义

查看：
```bash
which glm
ls -l /root/.local/bin/glm
grep "alias glm" ~/.bashrc
```

---

### Q5: 如何在 Python 代码中使用 API？
**A**:
```python
import os
from zhipuai import ZhipuAI

# 从环境变量读取
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = ZhipuAI(api_key=api_key)

# 使用 client 进行 API 调用
response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[{"role": "user", "content": "Hello"}]
)
```

使用 Anthropic SDK：
```python
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    base_url=os.environ.get("ANTHROPIC_API_BASE")
)
```

---

### Q6: 如何在 Node.js 中使用 API？
**A**:
```javascript
// 安装 SDK
// npm install @anthropic-ai/sdk

const Anthropic = require('@anthropic-ai/sdk');

const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
    baseURL: process.env.ANTHROPIC_API_BASE
});

// 使用 client 进行 API 调用
```

运行：
```bash
glm node your-app.js
```

---

### Q7: 可以在不同的目录使用 glm 命令吗？
**A**: 可以！`glm` 命令是全局可用的。

```bash
cd /tmp
glm python -c "import os; print(os.environ.get('ANTHROPIC_API_KEY')[:20])"
# ✅ 可以工作
```

---

### Q8: 如何更新 API 密钥？
**A**:
1. 编辑 `.env` 文件：
   ```bash
   nano /home/user/my-first-repo/.env
   ```

2. 修改密钥：
   ```bash
   ANTHROPIC_API_KEY="新的密钥"
   ```

3. 保存后立即生效（下次运行 `glm` 时会加载新密钥）

---

### Q9: 如何卸载/重新安装？
**A**:
```bash
# 删除符号链接
rm /root/.local/bin/glm

# 删除别名（编辑 ~/.bashrc，删除 glm 相关行）
nano ~/.bashrc

# 重新加载
source ~/.bashrc

# 重新安装
cd /home/user/my-first-repo
./install-glm-alias.sh
```

---

### Q10: 项目文件可以移动到其他目录吗？
**A**: 可以，但需要重新安装别名：

```bash
# 移动项目
mv /home/user/my-first-repo /new/location/

# 重新安装别名
cd /new/location/my-first-repo
./install-glm-alias.sh
source ~/.bashrc
```

---

## 📚 命令对照表

| 你可能想要的 | 正确的命令 | 说明 |
|-------------|-----------|------|
| `glm coding --init` | `chelper init` | 初始化配置向导 |
| `glm install` | `chelper enter claude-code` | 配置 Claude Code |
| `glm token set` | `chelper auth glm_coding_plan_china <token>` | 设置 API 密钥 |
| `glm update` | `git pull` | 更新脚本 |
| `glm --help` | `glm` 或 `chelper --help` | 查看帮助 |

---

## 🔍 工具对比

### 官方 glm CLI (xqsit94/glm)
- ❌ 无法安装（网络限制）
- ✅ 支持 `glm coding --init`
- ✅ 支持 `glm install claude`
- ✅ 自动配置 Claude Code

### 我们的 glm 脚本 (glm-start.sh)
- ✅ 已安装
- ✅ 自动加载环境变量
- ✅ 支持任何命令：`glm <command>`
- ❌ 不支持子命令（如 `coding --init`）

### coding-helper (chelper)
- ✅ 已安装
- ✅ 官方配置工具
- ✅ 支持 `chelper init`
- ⚠️ 需要网络连接

---

## ✅ 推荐工作流

### 首次配置（仅一次）
```bash
# 1. 设置中文（已完成）
chelper lang set zh_CN

# 2. 安装 glm 别名（已完成）
./install-glm-alias.sh
source ~/.bashrc

# 3. 验证配置
glm python test_glm.py
```

### 日常开发
```bash
# 开发 Python 项目
glm python my_app.py

# 开发 Node.js 项目
glm node server.js

# 安装依赖
glm pip install -r requirements.txt
glm npm install

# 运行测试
glm pytest
glm npm test
```

---

## 🆘 获取帮助

1. **查看文档**：
   ```bash
   cat README.md          # 完整文档
   cat SETUP_SUMMARY.md   # 配置总结
   cat DEMO.md            # 使用演示
   cat FAQ.md             # 本文档
   ```

2. **健康检查**：
   ```bash
   chelper doctor
   glm python -c "import os; print('✅ API Key:', os.environ.get('ANTHROPIC_API_KEY')[:20])"
   ```

3. **查看配置**：
   ```bash
   cat .env               # API 密钥
   which glm              # glm 命令位置
   chelper lang show      # chelper 语言设置
   ```

---

**💡 提示**：如果你遇到了这个 FAQ 没有涵盖的问题，请检查 README.md 或 SETUP_SUMMARY.md 文档！
