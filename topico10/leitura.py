path = "topico10/texto.txt"

with open(path, "r") as f:
    content = f.read()
    print(content)
    
    
with open(path, "r") as f:
    lst = [line.strip() for line in f if line.strip()]
    print(lst)