# ANALYST

We imported the dataset using, pandas library
convert data into pandas dataframe

clean some data ,

# Simple linear regression slr
relationship between predictor and target
y = c + mx
m is slope

we store parameters in numpy array 
each value goes in new row.

other factors also affect which is known
as noise . a small positive or negtive value
are added.

training points to get parameters.
we use these parameters to get a model.

it is a probability


# Multiple Linear Regression(MLR)
One continous target(Y)
two or more predictor(X)

Y = a + bx1 + cx2 + dx3 + ex4

1 extract predictor variables and store them in a variable
z = df[["horsepower", "curb- weight", "engine-size", "highway-mpg"]]

train as before

# 2 Regression Plot
When it comes to simple linear regression, an excellent way to visualize the fit of our model is by using regression plots.

This plot will show a combination of a scattered data points (a scatterplot), as well as the fitted linear regression line going through the data. This will give us a reasonable estimate of the relationship between the two variables, the strength of the correlation, as well as the direction (positive or negative correlation).

Residual Plot
A good way to visualize the variance of the data is to use a residual plot.

What is a residual?

The difference between the observed value (y) and the predicted value (Yhat) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.

So what is a residual plot?

A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.

What do we pay attention to when looking at a residual plot?

We look at the spread of the residuals:

- If the points in a residual plot are randomly spread out around the x-axis, then a linear model is appropriate for the data.

Why is that? Randomly spread out residuals means that the variance is constant, and thus the linear model is a good fit for this data.

# 3 pOLYNOMIAL REGRESSION
IT IS USED to create a curvilinear relationships
Model can be quadratic
y = a + bx +cx2
cubic 
noted by degrees.

calculate 3rd order
polyfit function
f = np.polyfit(x,y,3)
p = np.polyld(f)

We can print out the model
print(p)
# Pre processing
StandardScalar

# pipelines


# 4. Measures for In-Sample Evaluation
Two very important measures that are often used in Statistics to determine the accuracy of a model are:

R^2 / R-squared
Mean Squared Error (MSE)
# R-squared

R squared, also known as the coefficient of determination, is a measure to indicate how close the data is to the fitted regression line.

The value of the R-squared is the percentage of variation of the response variable (y) that is explained by a linear model.

# Mean Squared Error (MSE)

The Mean Squared Error measures the average of the squares of errors. That is, the difference between actual value (y) and the estimated value (ŷ).