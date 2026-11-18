import json
ficheiro = ("nomes.txt")


with open("dados.txt","r") as f:
    lista = f.readlines()
    for linha in lista:
        print(linha.strip())


with open(ficheiro,"w") as file:
    file.write("Gonçalo\n")
    file.write("Davi\n")


with open(ficheiro,"a") as file:
    file.write("Dinis\n")
    file.write("Davi\n")


with open("nomes.json", "r") as f:
    dados = json.load(f)


print (dados)
nome = {"nome": "Maria", "idade": 27}
dados.append(nome)


with open("nomes.json","w") as f:
    json.dump(dados,f,indent=4)