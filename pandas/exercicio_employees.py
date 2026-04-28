import pandas as pd

df_employees = pd.read_csv("employees.csv")

# limpar valores TOTALMENTE vazios
#df_employees = df_employees.dropna(how="all")

# Senior Management tipo booleano
#df_employees["Senior Management"] = df_employees["Senior Management"].astype("bool")

# Start Date e Last Login tipo datetime
#df_employees["Start Date"] = pd.to_datetime(df_employees["Start Date"])
#df_employees["Last Login Time"] = pd.to_datetime(df_employees["Last Login Time"])


df_employees["Gender"] = df_employees["Gender"].fillna("Não informado")

df_employees["Gender"].astype("category")



#print(df_employees["Gender"].isna())
print(df_employees.groupby(["Gender"])["Salary"].mean())