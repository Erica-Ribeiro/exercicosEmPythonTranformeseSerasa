#2) Faça um programa que recebe uma lista de números reais e exibe sua média

def calcular_media(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = soma / quantidade
    return media
lista_numeros = []
n = int(input("Informe a quantidade de números na lista: "))
for i in range(n):
    numero = float(input("Informe o número: " ))
    lista_numeros.append(numero)

media = calcular_media(lista_numeros)
print("A média dos números é:", media)