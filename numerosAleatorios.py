#7) Faça um programa que gere um número inteiro aleatório e que peça para o usuário adivinhar, 
# informe se o número que o usuário digitou é menor ou maior que o número gerado. O jogo acaba quando o usuário acertar o número gerado.
import random

numero_gerado = random.randint(1, 10)  # Gera um número aleatório entre 1 e 20

while True:
    palpite = int(input("Digite um número: "))

    if palpite == numero_gerado:
        print("Parabéns! Você acertou o número.")
        break
    elif palpite < numero_gerado:
        print("O número que você digitou é menor.")
    else:
        print("O número que você digitou é maior.")