import math

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

result = math.sqrt(math.pow(cateto_oposto,2) + math.pow(cateto_adjacente, 2))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print("A hipotenusa mede: {:.2f}".format(result))
print("Usando math.hypot o resultado é de: {:.2f}".format(hipotenusa))