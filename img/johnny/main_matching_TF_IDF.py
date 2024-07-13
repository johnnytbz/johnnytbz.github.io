import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 示例数据集
    data = {
        'company_name_1': ['ABC Corp', 'XYZ Ltd', 'ACME Corporation', '123 Industries', 'Alpha Limited', 'ABC Corp'],
        'company_name_2': ['xABC Corp', 'XYZ Limited', 'ACME Corp', '123 Industries', 'Alpha Ltd', 'ABC Corporation'],
        'label': [1, 1, 1, 1, 1, 1]  # 1表示匹配，0表示不匹配
    }

    df = pd.DataFrame(data)

    # 特征提取
    vectorizer = TfidfVectorizer()
    X1 = vectorizer.fit_transform(df['company_name_1'])
    X2 = vectorizer.transform(df['company_name_2'])

    # 合并特征
    X = np.abs(X1 - X2)  # 这里使用向量的绝对差来表示特征
    y = df['label']

    # 数据集划分
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 决策树模型
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # 模型预测
    y_pred = clf.predict(X_test)

    # 模型评估
    accuracy = accuracy_score(y_test, y_pred)
    print(f'模型准确率: {accuracy:.2f}')

    # 新的公司名称预测
    new_company_1 = 'ABC Corp'
    new_company_2 = 'xABC Corp'
    new_company_1_transformed = vectorizer.transform([new_company_1])
    new_company_2_transformed = vectorizer.transform([new_company_2])
    new_X = np.abs(new_company_1_transformed - new_company_2_transformed)

    prediction = clf.predict(new_X)

    print(f'公司名称1: {new_company_1}')
    print(f'公司名称2: {new_company_2}')
    print(f'预测结果: {"匹配" if prediction[0] == 1 else "不匹配"}')

    '''
    使用TF-IDF向量化结合机器学习
    1.数据准备：
        准备公司名称的数据集。
        标记匹配和不匹配的公司名称对。
    
    2.特征提取：
        使用TF-IDF向量化来表示公司名称。
    
    3.模型训练：
        使用机器学习算法（如决策树）来训练模型。
    '''
