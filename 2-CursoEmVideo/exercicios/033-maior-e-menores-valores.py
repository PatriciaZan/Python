num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

list = [num1, num2, num3]
bigger = max(list)
smaller = min(list)

print("O maior é {}".format(bigger))
print("O menor é {}".format(smaller))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3


menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3



print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
