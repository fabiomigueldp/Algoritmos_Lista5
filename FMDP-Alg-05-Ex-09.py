'''9. A string representa um inteiro? Neste exercício, você deve escrever uma função chamada
isInteger que determina se os caracteres em uma string representam ou não um inteiro válido,
retornando um valor lógico como resultado. Ao determinar se uma string representa um inteiro,
você deve ignorar qualquer espaço em branco à esquerda ou à direita. Uma vez que este
espaço em branco é ignorado, uma string representa um inteiro se seu comprimento for pelo
menos 1 e contiver apenas dígitos, ou se seu primeiro caractere for + ou - e o primeiro
caractere é seguido por um ou mais caracteres, todos os quais são dígitos. Escreva um
programa principal que leia uma string do usuário e informe se ela representa ou não um
número inteiro.

Dica: para concluir este exercício, você pode achar úteis os métodos lstrip, rstrip e/ou
strip do tipo de dados string. A documentação para esses métodos está disponível online.'''

def isInteger(string):
    string = string.strip()

    if len(string) == 0:
        return False

    if string[0] in "+-":
        string = string[1:] 

    if len(string) == 0:
        return False

    if not string.isdigit():
        return False

    return True

def main():
    string = input("Digite uma string: ")

    if isInteger(string):
        print("A string representa um número inteiro válido.")
    else:
        print("A string não representa um número inteiro válido.")

main()
