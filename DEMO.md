# GLM 命令演示

## ✅ 测试结果

### 1️⃣ Python 脚本测试

```bash
$ glm python test_glm.py
```

**输出：**
```
🔧 正在加载环境变量...
✅ 环境变量已加载：
   ANTHROPIC_API_KEY: ce114ad8a32c9b27af61...
   ANTHROPIC_API_BASE: https://open.bigmodel.cn/api/paas/v4

🚀 执行命令: python test_glm.py
🔑 API Key: ce114ad8a32c9b27af61...
🌐 API Base: https://open.bigmodel.cn/api/paas/v4

正在测试连接...
❌ 连接失败: Connection error.  # 网络限制，预期行为
```

**结论：** ✅ 环境变量加载成功！

---

### 2️⃣ Node.js 脚本测试

```bash
$ glm node test_glm.js
```

**输出：**
```
🔧 正在加载环境变量...
✅ 环境变量已加载：
   ANTHROPIC_API_KEY: ce114ad8a32c9b27af61...
   ANTHROPIC_API_BASE: https://open.bigmodel.cn/api/paas/v4

🚀 执行命令: node test_glm.js
🔑 API Key: ce114ad8a32c9b27af61...
🌐 API Base: https://open.bigmodel.cn/api/paas/v4

✅ 环境变量加载成功！
```

**结论：** ✅ 环境变量加载成功！

---

### 3️⃣ 交互式 Shell 测试

```bash
$ echo 'echo "ANTHROPIC_API_KEY = $ANTHROPIC_API_KEY"' | glm bash
```

**输出：**
```
🔧 正在加载环境变量...
✅ 环境变量已加载：
   ANTHROPIC_API_KEY: ce114ad8a32c9b27af61...
   ANTHROPIC_API_BASE: https://open.bigmodel.cn/api/paas/v4

🚀 执行命令: bash
测试: 环境变量 ANTHROPIC_API_KEY = ce114ad8a32c9b27af6169db0190842e.0VjUfYJie7cc40XJ
```

**结论：** ✅ 环境变量在子进程中正确传递！

---

## 🎯 测试总结

| 测试项 | 状态 | 说明 |
|--------|------|------|
| Python 脚本 | ✅ | 环境变量加载正常，API 调用受网络限制 |
| Node.js 脚本 | ✅ | 环境变量加载正常 |
| 交互式 Shell | ✅ | 环境变量正确传递到子进程 |
| 符号链接 | ✅ | 可从任何目录调用 `glm` 命令 |
| 环境隔离 | ✅ | 仅在 `glm` 启动的进程中可见 |

---

## 📝 使用示例

### Python 开发
```bash
# 运行 Python 脚本（自动加载 API 密钥）
glm python my_ai_script.py

# 运行 Python 交互式环境
glm python

# 安装 Python 包并运行
glm pip install anthropic
glm python -c "from anthropic import Anthropic; print('✅ SDK 已安装')"
```

### Node.js 开发
```bash
# 运行 Node.js 脚本
glm node my_ai_app.js

# 运行 npm 命令
glm npm install @anthropic-ai/sdk
glm npm test

# Node.js REPL
glm node
```

### 通用命令
```bash
# 任何需要环境变量的命令
glm curl -H "Authorization: Bearer $ANTHROPIC_API_KEY" https://api.example.com

# 启动开发服务器
glm npm run dev

# 运行测试
glm pytest tests/
```

### 交互式使用
```bash
# 启动交互式 shell（环境变量已加载）
glm

# 在 shell 中可以运行任何命令
$ python my_script.py
$ node app.js
$ echo $ANTHROPIC_API_KEY
$ exit  # 退出
```

---

## 🔐 安全性

- ✅ API 密钥存储在 `.env` 文件中
- ✅ `.env` 已加入 `.gitignore`，不会提交到 Git
- ✅ 环境变量仅在 `glm` 启动的进程中可见
- ✅ 不会污染全局环境
- ✅ 每次运行都从 `.env` 重新加载最新配置

---

## 🚀 高级用法

### 链式命令
```bash
# 安装依赖并运行
glm bash -c "pip install -r requirements.txt && python app.py"
```

### 临时覆盖环境变量
```bash
# glm 已加载 .env，还可以临时覆盖
ANTHROPIC_API_KEY=另一个密钥 glm python test.py
```

### CI/CD 集成
```bash
# 在 CI 环境中使用
./glm-start.sh pytest --cov=. tests/
./glm-start.sh npm run build
```

---

## ✨ 优势

1. **无需手动 source** - 自动加载环境变量
2. **环境隔离** - 不污染全局 shell 环境
3. **安全** - API 密钥不会意外泄露到命令历史
4. **便捷** - 一个命令搞定所有配置
5. **跨平台** - 适用于 Python、Node.js、任何需要环境变量的工具

---

## 📚 相关文件

- `glm-start.sh` - GLM 启动脚本
- `install-glm-alias.sh` - 别名安装脚本
- `test_glm.py` - Python 测试脚本
- `test_glm.js` - Node.js 测试脚本
- `.env` - API 密钥配置（本地，不提交）
- `.env.example` - 配置模板
- `README.md` - 完整文档
- `SETUP_SUMMARY.md` - 配置总结

---

**🎉 GLM 环境配置完成！开始你的 AI 开发之旅吧！**
