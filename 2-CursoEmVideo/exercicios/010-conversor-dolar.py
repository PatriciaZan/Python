dolar = 5.11

print("Conversor Reais X Dolar")
print("Dólar hoje {}".format(dolar))

print("="*20)
reais = int(input("Quantos reais você tem? : "))

result = reais / dolar

print("Você tem ${:.2f} dólares".format(result))