import pandas as pd
import numpy as np

path = "clean.csv"
#creating a dataframe using pandas with headers
df = pd.read_csv(path)

print(df[['price', 'horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])