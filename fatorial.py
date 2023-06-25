#4) Faça um programa que receba um número e exiba o fatorial desse número.
def calcular_fatorial(numero):
    fatorial = 1

    # Verifica se o número é negativo ou zero
    if numero < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    elif numero == 0:
        return "O fatorial de 0 é 1."

    # Calcula o fatorial do número
    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial

numero = int(input("Digite um número inteiro: "))

resultado = calcular_fatorial(numero)

print("O fatorial de", numero, "é:", resultado)