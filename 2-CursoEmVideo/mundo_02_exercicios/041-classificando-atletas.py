from datetime import date

birth_year = int(input("Digite o ano de nascimento: "))
current_year = date.today().year

age = current_year - birth_year

if age <= 9:
    print("MIRIM")
elif age <= 14:
    print("INFANTIL")
elif age <= 19:
    print("JUNIOR")
elif age <= 20:
    print("MASTER")