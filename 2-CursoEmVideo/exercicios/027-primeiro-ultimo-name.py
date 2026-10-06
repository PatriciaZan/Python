name = str(input("Digite o seu nome: "))

name_split = name.split()

print("O seu primeiro nome é {}".format(name_split[0]))
print("E seu ultimo nome é {}".format(name_split[-1]))