# ANALYST

We imported the dataset using, pandas library
convert data into pandas dataframe

clean some data ,
    first we provide names to the columns
    second we replace ? fields with Nan function of numpy for array calculations. np.NaN
    third we delete those rows with no price values.

we export data to a csv file with index off so no row no. be saved in the data.

other formats can be accessed using
csv 	pd.read_csv()	    df.to_csv()
json	pd.read_json()  	df.to_json()
excel	pd.read_excel()	    df.to_excel()
hdf 	pd.read_hdf()	    df.to_hdf()
sql	    pd.read_sql()	    df.to_sql()