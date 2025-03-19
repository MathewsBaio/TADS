#temp: float = float(input("temperatura em graus Fahrenheit? "));

def celsius(f: float):
    return (5/9) * (f - 32);

 
#print(f"A temperatura em graus Celsius é {celsius(temp):.2f}");


def trocaPU(ingredientes: list):
    aux = ingredientes[-1]
    ingredientes[-1] = ingredientes[0]
    ingredientes[0] = aux 
    return ingredientes

ingredientes: list = ['farinha', 'açúcar', 'manteiga', 'maçãs']
print(trocaPU(ingredientes))