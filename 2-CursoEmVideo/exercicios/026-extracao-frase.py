frase = str(input("Digite uma frase: "))

frase_lower = frase.lower()

print("A frase {}".format(frase))
print("Contém {} vezes a letra 'a'".format(frase_lower.count("a")))

print("-"*20)
print("A letra 'a' aparece primeiro na posição: {}".format(frase_lower.find("a")))

print("-"*20)
print("A letra 'a' aparece por ultimo na posição: {}".format(frase_lower.rfind("a")))