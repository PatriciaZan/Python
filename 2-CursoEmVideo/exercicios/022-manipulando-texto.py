name = str(input("Qual o seu nome completo? : "))

uppercase = name.upper()
print("Letras maiusculas: {}".format(uppercase))

lowercase = name.lower()
print("Letras minusculas: {}".format(lowercase))

length = name.replace(" ", "")
print("O seu nome tem {} letras".format(len(length)))

first_name_length = name.split()
print("O seu primeiro nome é {} e tem {} letras".format(first_name_length[0], len(first_name_length[0])))