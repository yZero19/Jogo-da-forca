import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():
    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print("Adivinhe a palavra abaixo:\n")
    print("Dica: Consoles/Aparelhos para jogar\n")

    palavras = ['playstation', 'xbox', 'nintendo', 'pc gamer']
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]
    chance = len(palavra) + 3
    letras_erradas = []

    while chance > 0:
        print(' '.join(letras_descobertas))
        print('\nChances restantes:', chance)
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            chance -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu! A palavra era:", palavra)
            break
    else:
        print("Você perdeu. A palavra era:", palavra)

if __name__ == "__main__":
    game()
    print("Esse é um jogo da forca feito em Python.")
