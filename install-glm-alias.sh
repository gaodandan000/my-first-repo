#!/bin/bash
# 安装 glm 命令别名

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GLM_SCRIPT="$SCRIPT_DIR/glm-start.sh"

echo "🔧 正在安装 glm 命令别名..."

# 检查脚本是否存在
if [ ! -f "$GLM_SCRIPT" ]; then
    echo "❌ 错误：glm-start.sh 不存在"
    exit 1
fi

# 添加别名到 .bashrc
if ! grep -q "alias glm=" ~/.bashrc 2>/dev/null; then
    echo "" >> ~/.bashrc
    echo "# GLM 启动脚本别名" >> ~/.bashrc
    echo "alias glm='$GLM_SCRIPT'" >> ~/.bashrc
    echo "✅ 已添加别名到 ~/.bashrc"
else
    echo "ℹ️  别名已存在于 ~/.bashrc"
fi

# 添加别名到 .zshrc（如果使用 zsh）
if [ -f ~/.zshrc ]; then
    if ! grep -q "alias glm=" ~/.zshrc; then
        echo "" >> ~/.zshrc
        echo "# GLM 启动脚本别名" >> ~/.zshrc
        echo "alias glm='$GLM_SCRIPT'" >> ~/.zshrc
        echo "✅ 已添加别名到 ~/.zshrc"
    else
        echo "ℹ️  别名已存在于 ~/.zshrc"
    fi
fi

echo ""
echo "✅ 安装完成！"
echo ""
echo "使用方法："
echo "  1. 重新加载配置: source ~/.bashrc"
echo "  2. 或者直接使用: $GLM_SCRIPT"
echo ""
echo "命令示例："
echo "  glm                  # 启动交互式 shell（环境变量已加载）"
echo "  glm python test_glm.py  # 运行 Python 脚本"
echo "  glm node script.js   # 运行 Node.js 脚本"
