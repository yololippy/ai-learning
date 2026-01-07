# Jupyter Notebook 与虚拟环境设置指南

## 为什么需要虚拟环境？

Jupyter Notebook 会使用启动时的 Python 环境。使用虚拟环境可以：
- ✅ 隔离项目依赖
- ✅ 避免版本冲突
- ✅ 保持系统 Python 干净
- ✅ 便于项目管理和分享

## 正确设置步骤

### 方法 1：在虚拟环境中安装和启动 Jupyter（推荐）

```bash
# 1. 创建虚拟环境
python3 -m venv venv

# 2. 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate      # Windows

# 3. 安装依赖（包括 Jupyter）
pip install -r requirements.txt

# 4. 启动 Jupyter（在虚拟环境中）
jupyter notebook
```

**优点**：简单直接，Jupyter 自动使用虚拟环境

### 方法 2：将虚拟环境注册为 Jupyter 内核

如果你已经有系统级的 Jupyter，可以这样设置：

```bash
# 1. 激活虚拟环境
source venv/bin/activate

# 2. 安装 ipykernel
pip install ipykernel

# 3. 注册虚拟环境为 Jupyter 内核
python -m ipykernel install --user --name=ai-learning --display-name "Python (AI Learning)"

# 4. 启动 Jupyter（可以从任何地方）
jupyter notebook

# 5. 在 Jupyter 界面中：
#    Kernel -> Change Kernel -> Python (AI Learning)
```

**优点**：可以在 Jupyter 中切换不同的 Python 环境

## 验证虚拟环境是否生效

在 Jupyter Notebook 中运行：

```python
import sys
print("Python 路径:", sys.executable)
print("虚拟环境:", 'venv' in sys.executable or 'env' in sys.executable)
```

如果显示虚拟环境路径，说明设置成功。

## 常见问题

### Q: 不用虚拟环境可以吗？
A: 技术上可以，但不推荐。会导致依赖冲突和管理困难。

### Q: Jupyter 找不到虚拟环境中的包？
A: 确保：
1. 在虚拟环境中安装了 Jupyter
2. 或者正确注册了内核
3. 在 Jupyter 中选择了正确的内核

### Q: 如何切换 Jupyter 使用的 Python 环境？
A: 在 Jupyter 界面：`Kernel -> Change Kernel -> 选择对应的内核`

## 最佳实践

1. ✅ **每个项目使用独立的虚拟环境**
2. ✅ **在虚拟环境中安装 Jupyter**
3. ✅ **使用 requirements.txt 管理依赖**
4. ✅ **不要将 venv/ 目录提交到 Git**

