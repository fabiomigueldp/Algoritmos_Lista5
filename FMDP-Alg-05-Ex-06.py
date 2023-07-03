'''Centralizando uma string. Escreva uma função que recebe uma string como seu primeiro
parâmetro e a largura de uma linha do terminal em caracteres como seu segundo parâmetro.
Sua função deve retornar uma nova string que consiste na string original e no número correto
de espaços iniciais para que a string original apareça centralizada dentro da largura fornecida
quando for impressa. Não adicione nenhum caractere ao final da string. Inclui um programa
principal que demonstre sua função.'''

def centralizar_string(texto, largura_linha):
    espacos_totais = largura_linha - len(texto)
    espacos_esquerda = espacos_totais // 2
    string_centralizada = " " * espacos_esquerda + texto
    return string_centralizada

def main():
    texto = input("Digite uma string: ")
    largura_linha = int(input("Digite a largura da linha do terminal em caracteres: "))
    string_centralizada = centralizar_string(texto, largura_linha)
    print("String centralizada:", string_centralizada)

main()
