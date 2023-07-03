'''Números ordinais. Palavras como primeiro, segundo e terceiro são chamadas de números
ordinais. Neste exercício, você deve escrever uma função que recebe um inteiro como seu
único parâmetro e retorna uma string contendo o número ordinal em português como seu
único resultado. Sua função deve lidar com números inteiros entre 1 e 12 (inclusive). Ela deve
retornar uma string vazia se um valor fora desse intervalo for fornecido como um parâmetro.
Inclua um programa principal que demonstra sua função exibindo cada inteiro de 1 a 12 e seu
respectivo número ordinal.'''

def obter_numero_ordinal(numero):
    if numero == 1:
        ordinal = "primeiro"
    elif numero == 2:
        ordinal = "segundo"
    elif numero == 3:
        ordinal = "terceiro"
    elif numero == 4:
        ordinal = "quarto"
    elif numero == 5:
        ordinal = "quinto"
    elif numero == 6:
        ordinal = "sexto"
    elif numero == 7:
        ordinal = "sétimo"
    elif numero == 8:
        ordinal = "oitavo"
    elif numero == 9:
        ordinal = "nono"
    elif numero == 10:
        ordinal = "décimo"
    elif numero == 11:
        ordinal = "undécimo"
    elif numero == 12:
        ordinal = "décimo segundo"
    else:
        ordinal = ""  # Retorna uma string vazia para valores fora do intervalo de 1 a 12
    return ordinal

def main():
    for i in range(1, 13):
        ordinal = obter_numero_ordinal(i)
        print(i, "=>", ordinal)

main()
