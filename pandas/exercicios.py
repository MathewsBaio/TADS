import pandas as pd

vendas = [
    ("2024-01-05", "Sudeste", "SP", 1500),
    ("2024-01-12", "Sul", "RS", 800),
    ("2024-01-18", "Nordeste", "BA", 1200),
    ("2024-02-03", "Sudeste", "RJ", 2000),
    ("2024-02-10", "Sul", "SC", 950),
    ("2024-02-15", "Nordeste", "PE", 750),
    ("2024-03-08", "Sudeste", "MG", 1800),
    ("2024-03-22", "Nordeste", "CE", 1100),
]

df_vendas = pd.DataFrame(vendas, columns=["Data", "Região", "Estado", "Valor"])

# Agrupando por Região e somando os valores
total_por_regiao = df_vendas.groupby("Região")["Valor"].sum().reset_index()

# print(total_por_regiao)


# Converter a coluna "Data" para datetime
df_vendas["Mes"] = pd.to_datetime(df_vendas["Data"]).dt.month_name()


# Agrupar por Ano/Mês e somar os valores
total_por_mes = df_vendas.groupby("Mes")["Valor"].sum().reset_index()

# print(total_por_mes)


subtotal_regiao_mes = df_vendas.groupby(["Região", "Mes"])["Valor"].sum().reset_index()

print(subtotal_regiao_mes)