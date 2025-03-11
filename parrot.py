count1 = 0
message = ""
numbers = []
while message != "quit":
    message = input("Digite um número ou quit para sair: ")
    if message != "quit":
        numbers.append(int(message))

print(f"Você digitou: {len(numbers)} números")    
print(f"Soma dos números digitados: {sum(numbers)}")

ordenados = sorted(numbers)
print(f"Os três maiores foram: {ordenados[-3:]}")

print("")    
print(sum(numbers))
