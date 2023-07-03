'''Tarifa do táxi. Em uma determinada cidade, as tarifas de táxi consistem em um valor inicial de
R$ 4,00 mais R$ 0,25 a cada 140 metros percorridos. Escreva uma função que recebe como
seu único parâmetro a distância percorrida em quilômetros, e retorna como seu único
resultado o valor total da corrida. Escreva um programa principal que demonstre o
funcionamento de sua função.'''

def calc_tarifa(valor_inicial, valor_por_distancia, distancia):
    distancia *= 1000
    distancia = distancia // 140
    tarifa = valor_inicial + (distancia * valor_por_distancia)
    return tarifa

def main():
    distancia = int(input("Insira a distância percorrida em km: "))
    tarifa = calc_tarifa(valor_inicial, valor_por_distancia, distancia)
    print("O valor total da viagem é de R$", tarifa)

valor_inicial = 4
valor_por_distancia = 0.25

main()