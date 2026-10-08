
salario = float(input("Qual é o salário? R$"))


aumento = 0

if salario > 1250:
    aumento = salario * 0.10
    print("O seu salário terá aumento de 10% ")
elif salario <= 1250:
    aumento = salario * 0.15
    print("O seu salário terá aumento de 15% ")

print("Seu salário aumenta em R${}".format(aumento))
print("Seu novo salário será de R${}".format(salario + aumento))
