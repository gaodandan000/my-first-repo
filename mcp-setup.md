# MCP Server 配置说明

## 🧋 Milk-Tea MCP Server

你想添加的命令：
```bash
claude mcp add -s user -t http milk-tea \
  https://open.bigmodel.cn/api/mcp/milk_tea/mcp \
  --header "Authorization: Bearer ce114ad8a32c9b27af6169db0190842e.0VjUfYJie7cc40XJ"
```

## ⚠️ 当前环境限制

`claude mcp add` 命令在当前环境中遇到问题：
- 可能需要网络连接来验证MCP服务器
- 可能需要交互式输入
- 命令一直挂起，无法完成

## ✅ 替代方案

### 方案1: 使用 chelper 配置（推荐）

chelper 可能有配置 MCP 的功能：

```bash
# 查看 chelper 的帮助
chelper --help

# 可能的配置入口
chelper enter
```

### 方案2: 手动配置文件

MCP 服务器配置通常保存在：
- `~/.claude/` 目录下
- 或者通过 `managed-mcp.json` 文件

可以查看是否有相关配置文件：
```bash
find ~/.claude -name "*mcp*" -type f
```

### 方案3: 在可访问网络的环境中运行

当你在正常网络环境中时，直接运行：
```bash
claude mcp add --scope user --transport http milk-tea \
  https://open.bigmodel.cn/api/mcp/milk_tea/mcp \
  --header "Authorization: Bearer ce114ad8a32c9b27af6169db0190842e.0VjUfYJie7cc40XJ"
```

### 方案4: 查看 MCP 列表

尝试查看当前已配置的 MCP 服务器：
```bash
claude mcp list
```

## 📚 MCP Server 信息

**名称**: milk-tea
**类型**: HTTP MCP Server
**URL**: https://open.bigmodel.cn/api/mcp/milk_tea/mcp
**认证**: Bearer Token (已配置)

## 🔍 验证配置

配置成功后，可以通过以下方式验证：

1. 列出 MCP 服务器：
   ```bash
   claude mcp list
   ```

2. 查看特定服务器：
   ```bash
   claude mcp get milk-tea
   ```

3. 在 Claude Code 中检查是否可用

## 💡 关于 Milk-Tea MCP Server

这似乎是智谱AI提供的一个 MCP 服务器，可能提供以下功能：
- AI 模型调用接口
- 特定领域的工具和功能
- 与 Claude Code 的集成

## 🆘 需要帮助？

如果需要更多帮助，可以：
1. 查看 Claude Code 官方文档
2. 查看智谱AI的 MCP 服务器文档
3. 在可访问网络的环境中重试配置

---

**配置时间**: 2025-12-26
**API Key**: ce114ad8a32c9b27af6169db0190842e.0VjUfYJie7cc40XJ
**状态**: ⏳ 等待在正常网络环境中配置
