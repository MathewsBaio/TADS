import pandas as pd


class Test:
    def __init__(self, atributo1):
        self.atributo1 = atributo1

name_data = ["Huguinho", "Zezinho", "Luizinho"]

obj = Test(12)

emps_names = pd.Series(name_data, index=["maaa",9001,obj])

email_data = ['huguinho.silva', "zezinho.pereira", "luizinho.santos"]

emps_emails = pd.Series(email_data,  index=["maaa",9001,obj], name="emails")

emps_names.name = "names"

df = pd.concat([emps_names, emps_emails], axis = 1) 

# axis 1 concatena na linha, criando uma tabela com uma coluna pra cada 'Series'

print(df)

