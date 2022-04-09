
# importing the pandas library
import pandas as pd
  
# reading the csv file
df = pd.read_csv("Rankings.csv")
  

# updating the column value/data
for year in range(85, 100):
	newYear = year + 1900
	df['Year'] = df['Year'].replace({year: newYear})
  
# writing into the file
df.to_csv("Rankings.csv", index=False)