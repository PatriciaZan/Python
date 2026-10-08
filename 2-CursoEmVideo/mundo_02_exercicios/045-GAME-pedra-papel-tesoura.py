import random
opcoes = ["pedra", "papel", "tesoura"]

#numb = random.randint(0, 2)

jogador = input("Escolha pedra, papel ou tesoura: ").lower().strip()

if jogador not in opcoes:
    print("Jogada inválida! Escolha apenas pedra, papel ou tesoura.")
else:
    computador = random.choice(opcoes)

    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (
            (jogador == "pedra" and computador == "tesoura")
            or (jogador == "papel" and computador == "pedra")
            or (jogador == "tesoura" and computador == "papel")
    ):
        print("Você venceu!")
    else:
        print("O computador venceu!")




