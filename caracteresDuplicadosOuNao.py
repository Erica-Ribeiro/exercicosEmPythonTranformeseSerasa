#5) Faça um programa que verifique se uma string possui caracteres duplicados.
def possui_caracteres_duplicados(string):
    caracteres = set()

    for char in string:
        if char in caracteres:
            return True
        caracteres.add(char)

    return False

string = input("Digite uma string: ")

if possui_caracteres_duplicados(string):
    print("A string possui caracteres duplicados.")
else:
    print("A string não possui caracteres duplicados.")