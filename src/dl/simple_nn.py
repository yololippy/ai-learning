"""
深度学习基础示例
使用 TensorFlow/Keras 创建简单的神经网络
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def create_simple_model(input_dim, num_classes):
    """
    创建一个简单的全连接神经网络
    """
    model = keras.Sequential([
        layers.Dense(128, activation='relu', input_shape=(input_dim,)),
        layers.Dropout(0.2),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model


def main():
    """
    使用 MNIST 数据集训练简单的神经网络
    """
    print("加载 MNIST 数据集...")
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.reshape(60000, 784).astype('float32') / 255.0
    x_test = x_test.reshape(10000, 784).astype('float32') / 255.0
    
    print(f"训练集形状: {x_train.shape}")
    print(f"测试集形状: {x_test.shape}")
    
    # 创建模型
    model = create_simple_model(input_dim=784, num_classes=10)
    model.summary()
    
    # 训练模型（这里只训练少量 epoch 作为示例）
    print("\n开始训练模型...")
    history = model.fit(
        x_train, y_train,
        batch_size=128,
        epochs=5,
        validation_split=0.1,
        verbose=1
    )
    
    # 评估模型
    print("\n评估模型...")
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"测试集准确率: {test_accuracy:.4f}")


if __name__ == "__main__":
    main()

