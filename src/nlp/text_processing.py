"""
自然语言处理基础示例
文本预处理和简单分析
"""

import re
from collections import Counter


def clean_text(text):
    """
    清理文本：移除标点符号，转换为小写
    """
    # 移除标点符号，只保留字母和空格
    text = re.sub(r'[^\w\s]', '', text)
    # 转换为小写
    text = text.lower()
    # 移除多余空格
    text = ' '.join(text.split())
    return text


def word_frequency(text):
    """
    统计词频
    """
    words = text.split()
    return Counter(words)


def main():
    """
    文本处理示例
    """
    sample_text = """
    Python is a powerful programming language. 
    Python is widely used in AI and machine learning.
    Many developers love Python for its simplicity.
    """
    
    print("原始文本:")
    print(sample_text)
    
    # 清理文本
    cleaned_text = clean_text(sample_text)
    print("\n清理后的文本:")
    print(cleaned_text)
    
    # 词频统计
    word_freq = word_frequency(cleaned_text)
    print("\n词频统计 (前10个):")
    for word, count in word_freq.most_common(10):
        print(f"  {word}: {count}")
    
    # 基本统计
    words = cleaned_text.split()
    print(f"\n总词数: {len(words)}")
    print(f"唯一词数: {len(set(words))}")
    print(f"平均词长: {sum(len(w) for w in words) / len(words):.2f}")


if __name__ == "__main__":
    main()

