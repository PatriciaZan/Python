print("calculadora para formar triângulos")

side1 = int(input("Digite o primeiro valor: "))
side2 = int(input("Digite o segundo valor: "))
side3 = int(input("Digite o terceiro valor: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Forma um triângulo")

    if side1 == side2 == side3:
        print("Triângulo: Equilátero")
    elif side1 != side2 != side3 != side1:
        print("Triângulo: Escaleno")
    elif side1 == side2 and side1 == side3 or side2 == side1 and side2 == side3:
        print("Triângulo: Isosceles")
else:
    print("Não forma um triângulo")