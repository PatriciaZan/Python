class User:
    def __init__(self,name,permission):
        self.name = name
        self.permission = permission

    # metodo
    def hello(self):
        print(f"Hello, {self.name}")

user1 = User("John","internal")
user2 = User("Mike","restricted")
user1.hello()


print(user1.name)
print(user1.permission)

class User2:
    def __init__(self,username,permission):
        self.username = username
        self.permission = permission

    def is_allowed(self):
        return self.permission in ["intern", "restricted"]

user = User2("Patricia", "intern")

print(user.username)
print(user.permission)

if user.is_allowed():
    print("User OK")

# ----------------------------------------------

try:
    number = int(input("digite um numero: "))
    print(number)
except ValueError:
    print("numero invalido")
finally:
    print("Finalizando")

# --------------------------

with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)































































