from requirements import plt,sns,pd,np,df, LinearRegression

print(df.head(2))
lm = LinearRegression()
X = df[["highway-mpg"]]
Y = df["price"]
lm.fit(X,Y)

YHAT = lm.predict(X)
print(df[["highway-mpg"]])
print(YHAT[0:5])

#Value of the intercept (a)?
lm.intercept_

# Value of the slope
lm.coef_

# final estimated linear model
# Price = 38423.31 - 821.73 x highway-mpg

# Multiple Linear regression

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])

lm.intercept_
lm.coef_

# Price = -15678.742628061467 + 52.65851272 * horsepower + 4.69878948 * curb-weight + 81.95906216 * engine-size + 33.58258185 * highway-mpg

lm2 = LinearRegression()
z = df[["normalized-losses", "highway-mpg"]]
lm2.fit(Z, df["price"])

lm2.coef_
lm2.intercept_