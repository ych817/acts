import pandas as pd
from sklearn.datasets import load_iris

# 加载数据
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 打印前 5 行
print(df.head())

# 打印所有花的名称（去重）
print("\nUnique species:")
print(df['species'].unique())
