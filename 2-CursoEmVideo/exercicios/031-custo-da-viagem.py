
distance = int(input("Qual a distancia da viagem? "))

if distance <= 200:
    print("Para viagens de até 200km o preço por km é de R$0,50")
    print("O valor da viajem fica R${}".format(distance * 0.50))
else:
    print("Para viagens de mais de 200km o preço por km é de R$0,45")
    print("O valor da viajem fica R${}".format(distance * 0.45))