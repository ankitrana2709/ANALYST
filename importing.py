import pandas as pd
# setting a file in a variable

path = "autos_import.data"
#creating a dataframe using pandas
df = pd.read_csv(path)

print(df.head())
#setting headers
#df.coloumn = headers