#!/bin/bash
# GLM API 启动脚本
# 模拟 glm CLI 工具功能：加载环境变量并启动 Claude Code

# 解析符号链接到实际脚本路径
SCRIPT_PATH="${BASH_SOURCE[0]}"
if [ -L "$SCRIPT_PATH" ]; then
    SCRIPT_PATH="$(readlink -f "$SCRIPT_PATH")"
fi
SCRIPT_DIR="$( cd "$( dirname "$SCRIPT_PATH" )" && pwd )"
ENV_FILE="$SCRIPT_DIR/.env"

# 检查 .env 文件是否存在
if [ ! -f "$ENV_FILE" ]; then
    echo "❌ 错误：.env 文件不存在"
    echo "请先创建 .env 文件并添加 API 凭证"
    exit 1
fi

echo "🔧 正在加载环境变量..."
# 读取 .env 文件并导出环境变量
set -a
source "$ENV_FILE"
set +a

echo "✅ 环境变量已加载："
echo "   ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:0:20}..."
echo "   ANTHROPIC_API_BASE: $ANTHROPIC_API_BASE"

# 如果提供了参数，执行该命令
if [ $# -gt 0 ]; then
    echo ""
    echo "🚀 执行命令: $@"
    exec "$@"
else
    # 否则启动交互式 shell
    echo ""
    echo "🚀 启动交互式 shell（环境变量已加载）"
    echo "   可以运行: claude code, python, node 等命令"
    echo "   退出: 输入 exit"
    exec bash
fi
