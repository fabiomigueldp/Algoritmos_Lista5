'''15. Dígitos hexadecimais e decimais. Escreva duas funções chamadas hex2int e int2hex,
que devem fazer a conversão entre dígitos hexadecimais (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D,
E e F) e números inteiros de base 10 . A função hex2int é responsável por converter uma
string contendo um único dígito hexadecimal em um inteiro de base 10, enquanto a função
int2hex é responsável por converter um inteiro entre 0 e 15 em um único dígito hexadecimal.
Cada função pegará o valor a ser convertido como seu único parâmetro e retornará o valor
convertido como o único resultado da função. Certifique-se de que a função hex2int funcione
corretamente para letras maiúsculas e minúsculas. Observação: se você não sabe como
converter números entre bases diferentes, veja o quadro explicativo ao final da lista de
exercícios.'''

def hex2int(hex_digit):
    hex_digit = hex_digit.upper()
    hex_digits = '0123456789ABCDEF'
    if hex_digit in hex_digits:
        return hex_digits.index(hex_digit)
    else:
        return None

def int2hex(decimal):
    hex_digits = '0123456789ABCDEF'
    if 0 <= decimal <= 15:
        return hex_digits[decimal]
    else:
        return None

def main():
    hex_digit = input("Digite um dígito hexadecimal: ")
    decimal = hex2int(hex_digit)
    if decimal is not None:
        print("O equivalente em decimal é:", decimal)
    else:
        print("Dígito hexadecimal inválido.")

    decimal = int(input("Digite um número entre 0 e 15: "))
    hex_digit = int2hex(decimal)
    if hex_digit is not None:
        print("O equivalente em hexadecimal é:", hex_digit)
    else:
        print("Número inválido.")

main()
