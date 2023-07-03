'''14. Datas mágicas. Uma “data mágica” é uma data na qual a multiplicação do dia pelo mês é
igual aos dois últimos dígitos do ano. Por exemplo, 10 de junho de 1960 é uma data mágica
porque 10 vezes 6 é igual a 60, que são os dois últimos dígitos do ano. Escreva uma função
que determina se uma data é ou não mágica. A função deve receber 3 parâmetros inteiros
(dia, mês e ano), e retornar um valor lógico. Escreva um programa main que utilize sua função
para determinar e imprimir todas as datas mágicas do século XX. O exercício anterior pode ser
útil para resolver este problema.'''

def isMagicDate(day, month, year):
    last_two_digits = year % 100
    return day * month == last_two_digits

def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
                if isMagicDate(day, month, year):
                    print(f"{day}/{month}/{year} é uma data mágica!")

main()
