# Author: Zhi Kai
# Time:  0:10
import pandas as pd
import openpyxl
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 从Excel文件中读取数据
file_name = "sentiment_data.xlsx"
df = pd.read_excel(file_name)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(df["Text"], df["Sentiment"], test_size=0.2, random_state=42)

# 文本特征提取
vectorizer = CountVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 训练情感分析模型
model = LogisticRegression(solver="liblinear", multi_class="ovr", random_state=42)
model.fit(X_train_vec, y_train)

# 评估模型性能
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 查看分类报告
report = classification_report(y_test, y_pred,zero_division=1)
print(report)

# 对新文本进行情感分析
sample_text = ["I love this product!", "This is terrible."]
sample_vec = vectorizer.transform(sample_text)
sample_pred = model.predict(sample_vec)
print("Predictions:", sample_pred)
