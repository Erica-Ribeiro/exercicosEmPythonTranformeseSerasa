#3) Dada uma lista de números inteiros, faça um programa que responda a soma de todos os números pares e ímpares.

def calcular_soma_pares_impares(lista):
    soma_pares = 0
    soma_impares = 0

    for numero in lista:
        if numero % 2 == 0:  # verifica se o número é par
            soma_pares += numero
        else:
            soma_impares += numero

    return soma_pares, soma_impares


lista_numeros = [1, 2, 7, 4, 5, 8, 20, 18, 29, 10]

soma_pares, soma_impares = calcular_soma_pares_impares(lista_numeros)

print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)