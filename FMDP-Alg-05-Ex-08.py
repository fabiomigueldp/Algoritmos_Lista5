'''8. Letras maiúsculas. Muitas pessoas não usam letras maiúsculas corretamente, especialmente
ao digitar em smartphones. Neste exercício, você escreverá uma função que coloca em
maiúscula os caracteres apropriados em uma string. O primeiro caractere da string deve ser
convertido em letra maiúscula, assim como o primeiro caractere (que não seja espaço) após
um “.”, “!” ou "?". Por exemplo, se a função for fornecida com a string “que horas eu tenho que
estar lá? qual é o endereço?" então ele deve retornar a string “Que horas eu tenho que estar
lá? Qual é o endereço?". Inclua um programa principal que leia uma string do usuário, corrige
as letras maiúsculas usando sua função e exibe o resultado.'''

def corrigir_maiusculas(frase):
    nova_frase = ""
    proximo_maiusculo = True

    for char in frase:
        if proximo_maiusculo and char.isalpha():
            nova_frase += char.upper()
            proximo_maiusculo = False
        else:
            nova_frase += char

        if char in ".!?":
            proximo_maiusculo = True

    return nova_frase

def main():
    frase = input("Digite uma frase: ")
    frase_corrigida = corrigir_maiusculas(frase)
    print("Frase com letras maiúsculas corrigidas:", frase_corrigida)

main()
