year = int(input("Digite um ano: "))

# Divisível por 4
# termina em 0
# e é divisível por 400

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("É um ano bissexto")
else:
    print("Não é ano bissexto")