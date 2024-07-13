import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle
import re

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 示例数据集
    data = {
        'company_name': ['ABC Corp', 'XYZ Ltd', 'ACME Corporation', '123 Industries', 'Alpha Limited'],
        'label': [1, 1, 0, 0, 1]  # 1表示匹配，0表示不匹配
    }

    df = pd.DataFrame(data)

    # 特征提取
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['company_name'])
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
    new_company = ['ABC Corp']
    new_company_transformed = vectorizer.transform(new_company)
    prediction = clf.predict(new_company_transformed)

    print(f'预测的公司名称: {new_company[0]}')
    print(f'预测结果: {"匹配" if prediction[0] == 1 else "不匹配"}')

    # 保存模型到 .pkl 文件
    with open('model_standardized.pkl', 'wb') as file:
        pickle.dump(clf, file)

    '''
    检查数据和模型训练步骤
    
    1.检查数据集：    
        确保数据集中的公司名称正确，并且标签（匹配或不匹配的标识）准确。
        数据是否经过必要的预处理（如清理、标准化等）？
    
    2.模型训练：    
        确保决策树模型训练过程正确。
        检查是否有足够的训练数据。
    
    3.特征提取：
        确保从公司名称中提取了正确的特征。
        例如，可以使用文本特征（如TF-IDF，n-grams）来表示公司名称。
    
    4.模型评估：    
        确保正确评估模型的性能，并使用适当的评估指标。
        
    常见问题
    1.数据样本量过少：
        数据样本量过少可能导致模型无法学习到有效的特征，尝试增加样本量。
    
    2.特征提取方式不当：
        使用适当的文本特征提取方法，如TF-IDF或词袋模型。
    
    3.模型参数调整：
        尝试调整决策树的参数，如max_depth、min_samples_split等，来提高模型性能。
    
    4.数据不平衡：
        如果正负样本不平衡，考虑使用class_weight参数或进行过采样/欠采样。
    
    示例代码总结
        确保数据准备、特征提取、模型训练和评估的每一步都正确执行。如果仍然有问题，请提供详细的代码和数据示例，以便进一步诊断问题。
    '''