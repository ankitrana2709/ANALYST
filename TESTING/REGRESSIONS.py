import pandas as pd
import numpy as np

path = "clean.csv"
#creating a dataframe using pandas with headers
df = pd.read_csv(path)

#Price=-7963.34 + 166.86*engine-size

#Price = -15678.742628061467 + 52.65851272 * horsepower + 4.69878948 * curb-weight + 81.95906216 * engine-size + 33.58258185 * highway-mpg