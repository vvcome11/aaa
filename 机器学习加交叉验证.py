import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv(r'D:\ning\five\ML\输入数据加分组.csv')

# 选择特征和目标变量
X = data.drop(columns=['SEQN', 'status', 'time', 'Cluster'])  # 特征列，去除不需要的列
y = data['status']  # 目标变量（假设是二分类问题）

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 初始化Logistic Regression模型，增加max_iter参数
model = LogisticRegression(max_iter=10000, random_state=42)

# 使用StratifiedKFold进行交叉验证，确保每个折叠中的类别比例与原始数据相同
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 使用cross_val_predict获取每个折叠的预测概率
y_pred_prob = cross_val_predict(model, X, y, cv=cv, method='predict_proba', n_jobs=-1)[:, 1]

# 计算ROC曲线
fpr, tpr, thresholds = roc_curve(y, y_pred_prob)
roc_auc = auc(fpr, tpr)
# 绘制ROC曲线
plt.rcParams['font.sans-serif'] = 'Arial'
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Logistic Regression (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.subplots_adjust(bottom=0.2)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel('False Positive Rate', fontsize=16)
plt.ylabel('True Positive Rate', fontsize=16)
plt.title('ROC Curve', fontsize=16, pad=10, loc='center')
plt.legend(loc='lower right', fontsize=14)
plt.show()

# 输出测试集AUC
print(f"finally AUC: {roc_auc:.4f}")
