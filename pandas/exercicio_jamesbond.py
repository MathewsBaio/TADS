import pandas as pd

df = pd.read_csv("jamesbond.csv")

# transformando coluna em indice, para buscar por valores especificos depois
#df = df.set_index(["Film","Year"])

#print(df.head())

# método loc faz busca por indices em texto, iloc faz por indices numericos
#print(df.loc[("Casino Royale", 2006)][["Actor", "Director"]])

df = df.dropna()
#print(df.groupby("Actor")["Bond Actor Salary"].sum())


#df = df.set_index("Actor")
#print(df.loc["David Niven"])


# Exemplo de consulta trazendo as 4 linhas com os maiores Box Office (bilheteria)
#print(df.nlargest(n=4, columns="Box Office")[["Film", "Year", "Box Office"]])


#mask = df["Actor"] == "Sean Connery"
#print(df[mask])


#Total de bilheteria dos filmes do james bond com o Daniel Craig

#mask = df["Actor"] == "Daniel Craig"
#print(df[mask]["Box Office"].sum())

df = df.reset_index()

def convert_to_millions_text(number):
    return str(number) + "millions"

df["Box Office M"] = df["Box Office"].apply(convert_to_millions_text)
print(df[["Film", "Box Office M"]])


# Buscar os três filmes mais antigos do James Bound.

# Bilheteria dos filmes por década