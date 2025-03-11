#m = [[i * j for j in range(1,4)] for i in range(1,4)]

lista = []

for i in range(1,4):
    linha = []
    for j in range(1,4):
        linha.append(i * j)
    lista.append(linha)

print(lista)

notas = [7,6,8,9,3,7,5,5]
print(sum(notas[:3]))

 
favorite_languages = {"Sarah": "C#", "Jon": "Java", "Carl": "PHP"}

for name, language in favorite_languages.items():
    print(f"\n{name}")

numero: int = 123