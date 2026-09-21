largura = int(input("Qual a largura da parede?: "))
altura = int(input("Qual a altura da parede?: "))

area = largura * altura

print("A área da parede é de {}m²".format(area))
print("Você vai precisar de {} litros de tinta".format(area/2))