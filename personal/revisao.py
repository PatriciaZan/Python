nome = "Patricia"
idade = 25

if idade >= 18:
    print("Maior de idade")
elif idade >= 16:
    print("Quase maior de idade")
else:
    print("Menor de idade")

## ------------------------------------------------------

usuario = "admin"
senha = "1234"

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso")
else:
    print("BLOCK")

## ------------------------------------------------------

names = ["Ana", "João", "Maria"]

for name in names:
    print(name)

for numero in range(1, 6): # vai até 5
    print(numero)

count = 0

while count < 5:
    print(count)
    count += 1

## ------------------------------------------------------
usuarios = ["Ana", "João", "Carlos"]
print(usuarios[0])

usuarios.append("Maria")

usuarios.remove("João")

for usuario in usuarios:
    print(usuario)

## ------------------------------------------------------
usuario2 = {
    "username": "carlos",
    "password": "1234",
    "permission": "intern"
}
# acessa
print(usuario2["username"])
#altera
usuario2["permission"] = "restricted"
#adiciona
usuario2["active"] = True

#percorrer
for key, value in usuario2.items():
    print(key, value)

## ------------------------------------------------------

def hello():
    print("Hello World")

hello()

def hello2(name2):
    print("Hello " + name2)
hello2("Patricia")

def sum(a,b):
    return a+b

resultSum = sum(2,3)
print(resultSum)

## ------------------------------------------------------



















