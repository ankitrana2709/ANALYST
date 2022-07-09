# WRANGLING

We imported the dataset using, pandas library
convert data into pandas dataframe

clean some data ,
    first we provide names to the columns
Steps for working with missing data:

Identify missing data
Deal with missing data
Correct data format
we export data to a csv file with index off so no row no. be saved in the data.

# Evaluating for Missing Data
The missing values are converted by default. We use the following functions to identify these missing values. There are two methods to detect missing data:

.isnull()
.notnull()
The output is a boolean value indicating whether the value that is passed into the argument is in fact missing data.

# Count missing values in each column
Using a for loop in Python, we can quickly figure out the number of missing values in each column. As mentioned above, "True" represents a missing value and "False" means the value is present in the dataset. In the body of the for loop the method ".value_counts()" counts the number of "True" values.

# Replace by mean:

"normalized-losses": 41 missing data, replace them with mean
"stroke": 4 missing data, replace them with mean
"bore": 4 missing data, replace them with mean
"horsepower": 2 missing data, replace them with mean
"peak-rpm": 2 missing data, replace them with mean
# Replace by frequency:

"num-of-doors": 2 missing data, replace them with "four".
Reason: 84% sedans is four doors. Since four doors is most frequent, it is most likely to occur
# Drop the whole row:

"price": 4 missing data, simply delete the whole row
Reason: price is what we want to predict. Any data entry without price data cannot be used for prediction; therefore any row now without price data is not useful to us

# Correct data format
In Pandas, we use:

.dtype() to check the data type

.astype() to change the data type

# Data Standardization
Data is usually collected from different agencies in different formats. (Data standardization is also a term for a particular type of data normalization where we subtract the mean and divide by the standard deviation.)

What is standardization?

Standardization is the process of transforming data into a common format, allowing the researcher to make the meaningful comparison.

# Data Normalization
Why normalization?

Normalization is the process of transforming values of several variables into a similar range. Typical normalizations include scaling the variable so the variable average is 0, scaling the variable so the variance is 1, or scaling the variable so the variable values range from 0 to 1.

# Binning
Why binning?
Binning is a process of transforming continuous numerical variables into discrete categorical 'bins' for grouped analysis.

# Indicator Variable (or Dummy Variable)
What is an indicator variable?
An indicator variable (or dummy variable) is a numerical variable used to label categories. They are called 'dummies' because the numbers themselves don't have inherent meaning.

Why we use indicator variables?

We use indicator variables so we can use categorical variables for regression analysis in the later modules.
# SAVING
other formats can be accessed using
csv 	pd.read_csv()	    df.to_csv()
json	pd.read_json()  	df.to_json()
excel	pd.read_excel()	    df.to_excel()
hdf 	pd.read_hdf()	    df.to_hdf()
sql	    pd.read_sql()	    df.to_sql()