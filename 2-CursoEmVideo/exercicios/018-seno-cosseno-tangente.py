import math

angulo = float(input("Didite o angulo em graus: "))

# 1. converter para radiano
angulo = math.radians(angulo)

# 2. calcular o seno
seno = math.sin(angulo)

# 3. calcular o cosseno
cosseno = math.cos(angulo)

# 4. calcular a tangente
tangente = math.tan(angulo)

print("O seno de {}º é {}".format(angulo,seno))
print("O cosseno de {}º é {}".format(angulo,cosseno))
print("A tangente de {}º é {}".format(angulo,tangente))


