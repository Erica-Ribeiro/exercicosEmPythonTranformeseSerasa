#1) Faça um programa que recebe uma lista de números reais e exibe o seu maior elemento.
x = 1
lista = []
print('Digite 3 números.')
while x <= 3:
    n = int(input('Digite um número: [ %s ]: '%x))
    lista.append(n)
    x += 1
print('O maior valor é:',max(lista))