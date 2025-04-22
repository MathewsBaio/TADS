import pandas as pd

dt = pd.read_csv("./dados/employees.csv").dropna(how="all")

# dt["Senior Management"] = dt["Senior Management"].astype("bool")
# dt["Start Date"] = pd.to_datetime(dt["Start Date"])
# dt["Last Login Time"] = pd.to_datetime(dt["Last Login Time"])


# print(dt.head())

# dt["Gender"] = dt["Gender"].astype("category")
# dt["Gender"] = dt["Gender"].fillna("NI")

# print(dt["Gender"].tail())


df_jamesbond = pd.read_csv("./dados/jamesbond.csv")

df_jamesbond = df_jamesbond.dropna(how="any")

df_jamesbond.set_index(["Film","Year"])

# print(df_jamesbond.loc[("Casino Royale",2006)])

df_bond_salary_actor = df_jamesbond.groupby("Actor")["Bond Actor Salary"].sum()

# print(df_bond_salary_actor)

mask = df_jamesbond["Actor"] == "Sean Connery"

# print(df_jamesbond[mask])

df_jamesbond.columns = [column_name.replace(" ","_") for column_name in df_jamesbond.columns]
print(df_jamesbond.query("Box_Office > 500"))
