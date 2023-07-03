'''16. Conversão arbitrária de base numérica. Escreva um programa que permita ao usuário
converter um número de uma base para base 10 e vice-versa. Seu programa deve suportar
bases entre 2 (binário) e 16 (hexadecimal) para o número de entrada e o número de resultado.
Divida seu programa em várias funções, incluindo uma função que converte de uma base
arbitrária em uma base 10, uma função que converte de uma base 10 em uma base arbitrária.
A primeira função deve receber como parâmetros uma string com o número a ser convertido
para base 10, e o valor da base deste número (portanto, de 2 a 16) e deve retornar como
resultado o número convertido na base 10. A segunda função deve receber como parâmetros
um numero na base 10 e a base para qual queremos converter o número. Como resultado, a
função deve retornar uma string com o número convertido. Além disso, faça um programa
principal que lê as bases e o número de entrada do usuário. Você pode encontrar parte da
solução deste problema no exercício anterior e nos exercícios 14 e 15 da lista 4.'''

def convert_to_decimal(number, base):
    decimal = 0
    power = 0
    digits = '0123456789ABCDEF'
    for digit in reversed(number):
        decimal += digits.index(digit) * (base ** power)
        power += 1
    return decimal

def convert_from_decimal(decimal, base):
    digits = '0123456789ABCDEF'
    if decimal == 0:
        return '0'
    result = ''
    while decimal > 0:
        digit = digits[decimal % base]
        result = digit + result
        decimal //= base
    return result

def main():
    number = input("Digite um número: ")
    base_input = int(input("Digite a base do número (2-16): "))
    decimal = convert_to_decimal(number, base_input)
    print("O número em decimal é:", decimal)

    base_output = int(input("Digite a base para conversão (2-16): "))
    result = convert_from_decimal(decimal, base_output)
    print("O número convertido é:", result)

main()