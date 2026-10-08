import random

numb = random.randint(0, 5)

print("Jogo da adivinhação")
print("Adivinhe um numero entre 0 e 5")
numb_user = int(input("Digite um numero entre 0 e 5: "))

if numb_user < numb:
    print("Você adivinhou baixo!")
    print("Numero sortiado {} | Seu numero {}".format(numb, numb_user))
elif numb_user > numb:
    print("Você adivinhou alto!")
    print("Numero sortiado {} | Seu numero {}".format(numb, numb_user))
elif numb_user == numb:
    print("Você acertou!")
    print("Numero sortiado {} | Seu numero {}".format(numb, numb_user))

