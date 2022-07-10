from wsgiref import headers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# setting a file in a variable

path = "clean_df.csv"
#creating a dataframe using pandas with no headers
df = pd.read_csv(path)

#Check top 5 rows
print(df.head(5))

#print(df.dtypes)
# we can calculate the correlation between variables of type "int64" or "float64" using the method "corr":
print(df.corr())
# the correlation between the following columns: bore, stroke, compression-ratio, and horsepower.
df[["bore","stroke","compression-ratio","horsepower"]].corr()


# SCATTER PLOT
# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
df[["engine-size", "price"]].corr()

# Highway mpg is a potential predictor variable of price. Let's find the scatterplot of "highway-mpg" and "price".
sns.regplot(x="highway-mpg", y="price", data=df)
df[['highway-mpg', 'price']].corr()

sns.regplot(x="peak-rpm", y="price", data=df)
df[['peak-rpm','price']].corr()

sns.regplot(x = "price", y = "stroke", data = df)
df[["stroke", "price"]].corr()

# BOX PLOTTING
sns.boxplot(x="body-style", y="price", data=df)

sns.boxplot(x="engine-location", y="price", data=df)

# drive-wheels
sns.boxplot(x="drive-wheels", y="price", data=df)

df.describe(include="all")
print(df.describe(include=['object']))

# using value counts
df['drive-wheels'].value_counts()
df['drive-wheels'].value_counts().to_frame()

# rename title
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts

# rename index
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts


# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1

grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot

#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()



from scipy import stats

pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  

grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)

# ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val)   