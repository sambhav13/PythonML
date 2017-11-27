import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn import decomposition
from sklearn import model_selection
df = pd.read_csv('D:\\MachineLearningVids\\data\\iris_df.csv')
df.columns = ['X1', 'X2', 'X3', 'X4', 'Y']
print(df.head())


from sklearn import decomposition
pca = decomposition.PCA()

fa = decomposition.FactorAnalysis()
X = df.values[:, 0:4]
Y = df.values[:, 4]
train, test = model_selection.train_test_split(X,test_size = 0.3)
train_reduced = pca.fit_transform(train)
test_reduced = pca.transform(test)
print("prediction:"+ str(pca.n_components_))

print(train_reduced)
print(fa)