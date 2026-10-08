print("Conversor de números inteiros")

numb = int(input("Digite um numero: "))

print("="*20)
print("Escolha qual base de conversão:")
print("1 - para binario")
print("2 - para octal")
print("3 - para hexadecimal")

choice = int(input("Sua escolha: "))

if choice == 1:
    print(bin(numb))
elif choice == 2:
    print(oct(numb))
elif choice == 3:
    print(hex(numb))
else:
    print("Escolha invalida")