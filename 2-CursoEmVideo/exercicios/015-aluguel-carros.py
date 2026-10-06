km_rodados = int(input("Quantos km rodados? "))
dias = int(input("Quantos dias usou o carro? "))

result = (dias * 60) + (km_rodados * 0.15)

print("O total a pagar é de R${}".format(result))