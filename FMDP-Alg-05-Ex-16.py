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
