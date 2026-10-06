name = str(input("Qual o seu nome? :"))

name_upper = name.upper()

if "SILVA" in name_upper:
    print("O seu nome {} tem 'SILVA".format(name))
else:
    print("O seu nome {} não tem 'SILVA'".format(name))