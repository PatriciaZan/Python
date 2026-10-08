speed = int(input("Qual a velocidade do carro?"))

value = 7

if speed > 80:
    above_speed = speed - 80
    print("Você foi multado! Sua velocidade de {}km/h ".format(speed))
    print("Para cada km/h aciam da velocidade de 80km/h permitidos você deve pagar R${}".format(value))
    print("Sua multa é de R${}".format(above_speed * value))
else:
    print("Você estava dentro do limite de velocidade de 80km/h")