from wsgiref import headers
import pandas as pd
import numpy as np
# setting a file in a variable

path = "autos_import.data"
#creating a dataframe using pandas with no headers
df = pd.read_csv(path, header=None)

#Check top 5 rows
#print(df.head(5))


#Check bottom ten rows
#print(df.tail(10))

#Marking Headers, We Create a list of headers for the data.
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
#print(headers)
# Placing headers as names of the coloumns.
df.columns = headers
# just checking these headers.
print(df.head(2))

# replace ? with NAN
df1 = df.replace("?", np.NaN)

# dropping missing price values
df= df1.dropna(subset=["price"], axis = 0)
print(df.head(10))

#saving dataset index false means row names are not written.
df.to_csv("Autombobile.csv", index=False)