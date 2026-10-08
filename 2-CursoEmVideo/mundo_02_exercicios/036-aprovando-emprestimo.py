valor_casa = float(input("Qual o valor da casa? R$"))
valor_salario = float(input("Qual é seu salário? R$"))
quantos_anos = int(input("Em quantos anos deseja pagar? "))

valor_prestacao = valor_casa / (quantos_anos * 12)

valor_maximo = valor_salario * 0.30

print("O valor da prestação é de R${:.2f}".format(valor_prestacao))
print("Você tem até 30% de seu salário como limite de valor de prestação = R${:.2f}".format(valor_maximo))

if valor_prestacao > valor_maximo:
    print("Seu empréstimo foi negado")
elif valor_prestacao < valor_maximo:
    print("Aprovado")