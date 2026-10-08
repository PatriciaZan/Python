preco_produto = float(input("Digite o valor do produto: R$ "))

print("Selecione sua forma de pagamento:")
print("1 - Dinheiro / PIX")
print("2 - Cartão")
print("3 - 2x cartão")
print("4 - 3x ou mais no cartão")

escolha = int(input("Digite sua forma de pagamento: "))

if escolha == 1:
    print("Dinheiro | PIX com 10% de desconto")
    desconto = preco_produto - (preco_produto * 10 / 100)
    print("O Valor de desconto é de R${}".format(desconto))
    print("O valor final é de R${}".format(preco_produto - desconto))
elif escolha == 2:
    print("Cartão com 5% de desconto")
    desconto = preco_produto - (preco_produto * 5 / 100)
    print("O Valor de desconto é de R${}".format(desconto))
    print("O valor final é de R${}".format(preco_produto - desconto))
elif escolha == 3:
    print("2x Cartão preço normal")
    print("Sem desconto")
    print("O valor final é de R${}".format(preco_produto))
elif escolha == 4:
    print("3x ou mais no cartão com 20% de juros")
    juros = preco_produto - (preco_produto * 10 / 100)
    print("O Valor de desconto é de R${}".format(juros))
    print("O valor final é de R${}".format(preco_produto + juros))


