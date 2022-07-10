import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression

path = "clean.csv"
#creating a dataframe using pandas with headers
df = pd.read_csv(path)

# regression plot
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x = "highway-mpg", y = "price", data = df)
plt.ylim(0,)

plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)

plt.show()

# residual plot
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(df['highway-mpg'], df['price'])
plt.show()

# distribution plot for multiple regression

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm = LinearRegression()
lm.fit(Z, df['price'])
Y_hat = lm.predict(Z)

plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()