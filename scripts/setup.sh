#!/bin/bash
# GLM Coding 环境设置脚本
# GLM Coding Environment Setup Script

echo "GLM Coding 环境设置 / GLM Coding Environment Setup"
echo "=================================================="

# 检查Python版本
echo "检查Python版本 / Checking Python version..."
python3 --version

# 创建虚拟环境
echo ""
echo "创建虚拟环境 / Creating virtual environment..."
python3 -m venv venv

# 激活虚拟环境
echo ""
echo "激活虚拟环境 / Activating virtual environment..."
source venv/bin/activate

# 安装依赖
echo ""
echo "安装依赖 / Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 创建日志目录
echo ""
echo "创建日志目录 / Creating logs directory..."
mkdir -p logs

# 创建模型目录
echo ""
echo "创建模型目录 / Creating models directory..."
mkdir -p models
touch models/.gitkeep

# 复制环境变量模板
if [ ! -f .env ]; then
    echo ""
    echo "复制环境变量模板 / Copying .env template..."
    cp .env.example .env
    echo "请编辑 .env 文件并设置你的 GLM_API_KEY"
    echo "Please edit .env file and set your GLM_API_KEY"
fi

echo ""
echo "=================================================="
echo "✓ 设置完成！/ Setup completed!"
echo ""
echo "下一步 / Next steps:"
echo "1. 编辑 .env 文件并设置你的 GLM_API_KEY"
echo "   Edit .env file and set your GLM_API_KEY"
echo ""
echo "2. 运行示例程序："
echo "   Run example:"
echo "   python examples/basic_glm_usage.py"
echo ""
echo "3. 查看文档："
echo "   View documentation:"
echo "   cat README.md"
