#!/bin/bash

# Python AI 学习项目环境设置脚本

echo "🚀 开始设置 Python AI 学习环境..."

# 检查 Python 版本
echo "📋 检查 Python 版本..."
python3 --version

# 创建虚拟环境
echo "📦 创建虚拟环境..."
python3 -m venv venv

# 激活虚拟环境
echo "✅ 激活虚拟环境..."
source venv/bin/activate

# 升级 pip
echo "⬆️  升级 pip..."
pip install --upgrade pip

# 安装依赖
echo "📥 安装项目依赖..."
pip install -r requirements.txt

echo ""
echo "✨ 环境设置完成！"
echo ""
echo "📝 重要提示："
echo "   Jupyter Notebook 必须在虚拟环境中启动，才能使用虚拟环境中的包！"
echo ""
echo "🚀 使用步骤："
echo "   1. 激活虚拟环境:"
echo "      source venv/bin/activate"
echo ""
echo "   2. 启动 Jupyter Notebook（在虚拟环境中）:"
echo "      jupyter notebook"
echo ""
echo "   3. 验证虚拟环境（在 Jupyter 中运行）:"
echo "      import sys"
echo "      print(sys.executable)  # 应该显示 venv 路径"
echo ""

