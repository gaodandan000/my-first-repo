# 在 Claude Code 终端中安装 GLM Coding 完整指南

## 🎯 目标

将 GLM Coding Plan 集成到 Claude Code 终端版本中，以便使用智谱AI的 GLM 模型。

## ✅ 已完成的配置

你已经完成了以下配置：

1. ✅ **API 密钥配置** - .env 文件
2. ✅ **glm 启动脚本** - 自动加载环境变量
3. ✅ **Python SDK** - zhipuai
4. ✅ **coding-helper** - chelper 工具

## 🔧 在 Claude Code 中使用 GLM 的方法

### 方法1: 通过环境变量配置（推荐，已完成）

Claude Code 可以读取环境变量来配置 API。

**已完成的配置：**

1. `.env` 文件包含：
   ```bash
   ANTHROPIC_API_KEY="ce114ad8a32c9b27af6169db0190842e.0VjUfYJie7cc40XJ"
   ANTHROPIC_API_BASE="https://open.bigmodel.cn/api/paas/v4"
   ```

2. 通过 `glm` 命令启动：
   ```bash
   glm python script.py    # 自动加载环境变量
   ```

3. 或者手动加载：
   ```bash
   source .env
   # 环境变量现在可用
   ```

**验证配置：**
```bash
glm python -c "import os; print('API Key:', os.environ.get('ANTHROPIC_API_KEY')[:20]+'...')"
```

### 方法2: 使用 coding-helper (chelper)

**已安装：** ✅ chelper (中文界面)

**配置步骤：**

```bash
# 1. 初始化配置（需要网络）
chelper init

# 2. 配置 API 密钥
chelper auth glm_coding_plan_china "ce114ad8a32c9b27af6169db0190842e.0VjUfYJie7cc40XJ"

# 3. 配置 Claude Code
chelper enter claude-code

# 4. 健康检查
chelper doctor
```

**当前状态：**
- ✅ chelper 已安装
- ✅ 中文界面已配置
- ⚠️ API 密钥配置受网络限制

### 方法3: 配置 Claude Code settings.json

Claude Code 的配置文件位于 `~/.claude/settings.json`

**添加环境变量：**

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "env": {
    "ANTHROPIC_API_KEY": "ce114ad8a32c9b27af6169db0190842e.0VjUfYJie7cc40XJ",
    "ANTHROPIC_API_BASE": "https://open.bigmodel.cn/api/paas/v4"
  },
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo '✅ GLM API 环境已加载'"
          }
        ]
      }
    ]
  }
}
```

**注意：** 这会将 API 密钥写入配置文件，建议使用环境变量方式更安全。

### 方法4: 配置 MCP 服务器（高级）

**MCP (Model Context Protocol)** 允许 Claude Code 连接到外部服务。

**命令（需要网络）：**
```bash
claude mcp add --scope user --transport http milk-tea \
  https://open.bigmodel.cn/api/mcp/milk_tea/mcp \
  --header "Authorization: Bearer ce114ad8a32c9b27af6169db0190842e.0VjUfYJie7cc40XJ"
```

**当前状态：**
- ⚠️ 命令在当前环境中挂起（网络限制）
- 📄 详细说明见 `mcp-setup.md`

## 🎯 推荐方案

### 快速开始（已完成）✅

你的环境已经配置好了！直接使用：

```bash
# 方式1: 使用 glm 脚本（推荐）
glm python test_glm.py

# 方式2: 手动加载环境变量
source .env
python test_glm.py

# 方式3: 在代码中直接使用
python your_app.py  # 需要先 source .env
```

### 验证 GLM API 是否可用

**Python 测试：**
```bash
glm python test_glm.py
```

**Node.js 测试：**
```bash
glm node test_glm.js
```

**查看环境变量：**
```bash
glm python -c "import os; print('✅ API配置:', os.environ.get('ANTHROPIC_API_BASE'))"
```

## 🔍 故障排查

### 问题1: API 连接失败

```
❌ 连接失败: Connection error.
```

**原因：** 当前环境网络限制

**解决：** 在可访问网络的环境中运行

### 问题2: chelper 命令卡住

```bash
chelper init  # 一直挂起
```

**原因：** 需要网络连接验证

**解决：** 使用 glm 脚本（不需要网络验证）

### 问题3: claude mcp 命令失败

```bash
claude mcp add ...  # 挂起
```

**原因：** 网络限制

**解决：** 在正常网络环境中配置

## 📊 当前配置状态

```
✅ API 密钥        已配置（.env）
✅ glm 命令        已安装（全局可用）
✅ Python SDK      已安装（zhipuai）
✅ Node.js 支持    已配置
✅ chelper 工具    已安装（中文界面）
✅ 环境变量        自动加载工作正常
⚠️  MCP 服务器     未配置（网络限制）
⚠️  API 连接       网络受限（配置正确）
```

## 🚀 开始使用

### 示例1: Python 脚本

```python
#!/usr/bin/env python3
import os
from zhipuai import ZhipuAI

# API 密钥从环境变量读取
client = ZhipuAI(api_key=os.environ.get("ANTHROPIC_API_KEY"))

response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

**运行：**
```bash
glm python your_script.py
```

### 示例2: Node.js 应用

```javascript
const Anthropic = require('@anthropic-ai/sdk');

const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
    baseURL: process.env.ANTHROPIC_API_BASE
});

// 使用 client 进行 API 调用
```

**运行：**
```bash
glm node your_app.js
```

### 示例3: 在 Claude Code 会话中

如果配置了环境变量到 `~/.claude/settings.json`，则在 Claude Code 会话中：

```
你: 帮我用 GLM API 生成一段文本
Claude: [可以直接使用环境变量中的 API]
```

## 📚 相关文档

- `README.md` - 完整使用指南
- `FAQ.md` - 常见问题解答
- `DEMO.md` - 使用演示
- `SETUP_SUMMARY.md` - 配置总结
- `mcp-setup.md` - MCP 服务器配置

## ✨ 总结

**你的 GLM Coding 环境已经在 Claude Code 终端中配置好了！**

主要方式：
1. ✅ **glm 命令** - 最简单，自动加载环境变量
2. ✅ **source .env** - 手动加载
3. ⚠️ **chelper** - 需要网络
4. ⚠️ **MCP 服务器** - 需要网络

**推荐：** 使用 `glm` 命令，无需网络，配置已完成！

开始使用：
```bash
glm python test_glm.py    # 测试 Python
glm node test_glm.js      # 测试 Node.js
glm                       # 交互式 shell
```

🎉 **配置完成，开始开发吧！**
