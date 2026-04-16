import pandas as pd

nba = pd.read_csv("nba.csv")   

print(nba.head())

#nba = nba.dropna()

#print(nba.groupby("College")["Salary"].mean())

print(nba.dropna(how="all").info())