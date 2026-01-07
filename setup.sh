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
echo "要激活虚拟环境，请运行:"
echo "  source venv/bin/activate"
echo ""
echo "要启动 Jupyter Notebook，请运行:"
echo "  jupyter notebook"
echo ""

