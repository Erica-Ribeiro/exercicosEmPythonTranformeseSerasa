#6) Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. Caso a média seja igual ou superior a 7, 
# apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. Caso a nova média seja igual
# superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media


notas = []
for i in range(4):
    nota = float(input(f"Informe a nota {i + 1}: "))
    notas.append(nota)

media = calcular_media(notas)

if media >= 7:
    print("APROVADO")
else:
    nota_final = float(input("Informe a nota da prova final: "))
    notas.append(nota_final)
    nova_media = calcular_media(notas)

    if nova_media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")