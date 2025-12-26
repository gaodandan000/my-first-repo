# my-first-repo
用来存我的AI项目/脚本/文档

## 设置 Anthropic API

### 环境变量配置

1. 复制 `.env.example` 到 `.env`:
   ```bash
   cp .env.example .env
   ```

2. 编辑 `.env` 文件，填入你的API凭证

3. 加载环境变量:
   ```bash
   source .env
   # 或者
   export $(cat .env | xargs)
   ```

### 使用方法

在你的脚本中可以这样使用:

**Python:**
```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    base_url=os.environ.get("ANTHROPIC_API_BASE")
)
```

**Node.js:**
```javascript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
  baseURL: process.env.ANTHROPIC_API_BASE
});
```

**注意:** `.env` 文件已被添加到 `.gitignore`，不会被提交到版本控制中。

## 已安装的工具

### 1. zhipuai (Python SDK)
```bash
pip install zhipuai  # 已安装
```

### 2. coding-helper (CLI 工具)
```bash
npm install -g @z_ai/coding-helper  # 已安装
chelper init  # 运行初始化向导
```

## 测试API连接

运行测试脚本：
```bash
source .env  # 加载环境变量
python test_glm.py  # 测试连接
```

## GLM 启动脚本

由于网络限制无法安装官方的 `glm` CLI 工具，我们提供了一个替代脚本：

### 方式1: 直接使用脚本
```bash
./glm-start.sh              # 启动交互式 shell
./glm-start.sh python test_glm.py  # 运行 Python 脚本
```

### 方式2: 安装别名（推荐）
```bash
./install-glm-alias.sh      # 安装 glm 命令别名
source ~/.bashrc            # 重新加载配置

# 然后就可以使用 glm 命令了
glm                         # 启动交互式 shell
glm python test_glm.py      # 运行测试脚本
```

## 常见问题

**Q: `glm coding --init` 命令不存在？**
A: 这个命令不存在。正确的方式是：
- 使用 `chelper init`（需要网络）
- 或使用我们提供的 `glm-start.sh` 脚本（本地方案）

**Q: `chelper auth` 提示网络错误？**
A: 由于网络限制，无法验证API密钥。建议直接使用 `glm-start.sh` 脚本，它会自动加载 `.env` 中的环境变量。

**Q: 如何配置 Claude Code？**
A: Claude Code 会自动读取环境变量 `ANTHROPIC_API_KEY` 和 `ANTHROPIC_API_BASE`。使用 `glm-start.sh` 脚本启动即可。
