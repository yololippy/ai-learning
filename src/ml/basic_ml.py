"""
机器学习基础示例
使用 scikit-learn 进行简单的分类任务
"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def main():
    """
    使用鸢尾花数据集进行简单的分类任务
    """
    # 加载数据集
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    
    print("数据集形状:", X.shape)
    print("类别数量:", len(np.unique(y)))
    print("类别名称:", iris.target_names)
    
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"\n训练集大小: {X_train.shape[0]}")
    print(f"测试集大小: {X_test.shape[0]}")
    
    # 创建并训练模型
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    
    # 评估
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n模型准确率: {accuracy:.4f}")
    print("\n分类报告:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))


if __name__ == "__main__":
    main()

