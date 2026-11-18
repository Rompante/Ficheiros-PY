# f = open("dados.txt")
# lista = f.readlines()

# for linha in lista:
#     print(linha.strip())

# f.close()

with open("dados.txt", "r") as f:
    lista = f.readlines()
    for linha in lista:
        print(linha.strip())

with open("nomes.txt" , "w") as file:
    file.write("Marcelo\n")
    file.write("Ana\n")