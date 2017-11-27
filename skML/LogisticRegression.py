import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

from sklearn.linear_model import LogisticRegression


df = pd.read_csv('D:\\MachineLearningVids\\data\\logistic_regression_df.csv')
df.columns = ['X', 'Y']
df.head()


sns.set_context('notebook', font_scale=1.1)
sns.set_style('ticks')
sns.regplot('X','Y', data=df, logistic=True)
plt.ylabel('Probability')
plt.xlabel('Explanatory')

logistic = LogisticRegression()
X = (np.asarray(df.X)).reshape(-1, 1)
Y = (np.asarray(df.Y)).ravel()
logistic.fit(X, Y)
logistic.score(X, Y)
print('Coefficient: \n', logistic.coef_)
print('Intercept: \n', logistic.intercept_)
print('R² Value: \n', logistic.score(X, Y))
plt.show()