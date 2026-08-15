

# Python AI 学习项目

这是一个用于学习 Python 和人工智能相关知识的项目。

## 项目结构

```
ai/
├── README.md                 # 项目说明
├── requirements.txt          # Python 依赖包
├── .gitignore               # Git 忽略文件
├── notebooks/               # Jupyter Notebook 学习笔记
├── src/                     # 源代码目录
│   ├── basics/              # Python 基础
│   ├── ml/                  # 机器学习
│   ├── dl/                  # 深度学习
│   └── nlp/                 # 自然语言处理
├── data/                    # 数据文件目录
└── models/                  # 模型保存目录
```

## 环境设置

### 1. 创建虚拟环境

```bash
# 使用 venv
python3 -m venv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 启动 Jupyter Notebook

```bash
# 请确保已在当前终端激活了虚拟环境
jupyter notebook
```

## 学习路径

### Python 基础
- 基本语法和数据类型
- 面向对象编程
- 文件操作和异常处理
- 常用标准库

### 机器学习
- 数据预处理
- 监督学习（分类、回归）
- 无监督学习（聚类、降维）
- 模型评估和优化

### 深度学习
- 神经网络基础
- TensorFlow/Keras
- PyTorch
- CNN、RNN、Transformer

### 自然语言处理
- 文本预处理
- 词向量
- 语言模型
- 文本分类和生成

## 资源推荐

- [Python 官方文档](https://docs.python.org/zh-cn/3/)
- [Scikit-learn 文档](https://scikit-learn.org/stable/)
- [TensorFlow 教程](https://www.tensorflow.org/tutorials)
- [PyTorch 教程](https://pytorch.org/tutorials/)

## 许可证

ISC
