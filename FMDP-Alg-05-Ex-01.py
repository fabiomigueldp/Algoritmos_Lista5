'''1. Hipotenusa. Escreva uma função que recebe como parâmetros os comprimentos dos dois
lados menores de um triângulo retângulo. A função deve retornar como resultado o
comprimento da hipotenusa, calculado com o Teorema de Pitágoras. Inclua um programa
principal (função main) que solicite ao usuário os comprimentos dos lados, utilize sua função
para calcular a hipotenusa e imprima o resultado.'''

import math

def hip(a, b):
    hipotenusa = math.sqrt(a**2+b**2)
    return hipotenusa
    

def main ():
    a = float(input("Insira o comprimento do primeiro cateto: "))
    b = float(input("Insira o comprimente do segundo cateto: "))
    hipotenusa = hip(a, b)
    print("A hipotenusa do triângulo é: ", hipotenusa)
    
    

main()