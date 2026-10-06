import random

# versão 1
alunos = ["João", "Maria", "Alex", "Luiza"]
numb = random.randint(0, 3)
print("O aluno sortiado foi: {}".format(alunos[numb]))

print("="*20)
print("Versão 2")

#versão 2

n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))


list = [n1,n2,n3,n4]
chosen = random.choice(list)
print("O aluno sorteado foi {}".format(chosen))
