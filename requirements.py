import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression

path = "clean.csv"
#creating a dataframe using pandas with headers
df = pd.read_csv(path)
