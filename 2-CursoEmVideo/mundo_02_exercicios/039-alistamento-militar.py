from datetime import date

birth_year = int(input("Digite o ano de nascimento: "))

current_year = date.today().year

print(current_year)
age = current_year - birth_year
print(age)

if age < 18:
    print("Você ainda tem que se alistar em {} anos".format(age - 18))
elif age == 18:
    print("Você tem que se alistar")
elif age > 18:
    print("Você já deveria ter se alistado faz {} anos".format(age - 18))
