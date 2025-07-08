# Importações
import random
from time import sleep
from .. import ui

# Função Principal
def sorteio():
    """
    -> Mostra as opções de sorteio, pede ao usuário escolher alguma, e executa a função referente a escolha do usuário.
    """
    try:
        while True:
            opções = [
                'Voltar',
                'Gerador de Senhas Alphanuméricas',
                'Gerador de Senhas Alphanuméricas com Caracteres Especiais',
            ]
            ui.menu(opções, 'Gerador de Senhas')
            resposta = int(input('Escolha: '))
            if resposta == 0:
                ui.cabeçalho('VOLTANDO AO MENU PRINCIPAL...')
                break

            elif resposta == 1:
                gerador_senha_alphanumérica()

            elif resposta == 2:
                gerador_senha_alphanumérica_caracteres()

            else:
                print('\033[0;31mERRO! Digite uma opção válida.\033[m')
        return
    except resposta is float or str:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')

    except KeyboardInterrupt:
        return

def gerador_senha_alphanumérica():
    """
    -> Pede ao usuário a quantidade de caracteres a serem sorteados. O programa sorteia números inteiros e adiciona a uma lista os caracteres referentes ao número sorteado em uma lista de caracteres alphanuméricos pré-definidos.
    """
    max_chars = int(input('Digite a quantidade de caracteres: '))
    password = []
    caracteres = (
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
        'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
        'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
        'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'
    )
    for _ in range(max_chars):
        sorteado = random.randint(0, len(caracteres) - 1)
        password.append(caracteres[sorteado])
    for c in password:
        ui.resultado(valor=c)
    print()

def gerador_senha_alphanumérica_caracteres():
    """
    -> Pede ao usuário a quantidade de caracteres a serem sorteados. O programa sorteia números inteiros e coloca em uma lista os caracteres referentes pré-declarados em uma lista.
    """
    max_chars = int(input('Digite a quantidade de caracteres: '))
    password = []
    caracteres = (
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
        'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
        'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
        'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z',
        '?', '!', '@', '#', '$', '%', '/', '+', '-', '_', '=', '*', '&', '<',
        '>', '(', ')', '[', ']', '{', '}', 'Ç', 'ç'
    )
    for _ in range(max_chars):
        sorteado = random.randint(0, len(caracteres) - 1)
        password.append(caracteres[sorteado])
    for c in password:
        ui.resultado(valor=c, linhas=False)
    print()
