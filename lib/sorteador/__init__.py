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
                'Sorteio de Números',
                'Gerador de Nomes'
            ]
            ui.menu(opções, 'Sorteio')
            resposta = int(input('Escolha: '))
            if resposta == 0:
                ui.cabeçalho('VOLTANDO AO MENU PRINCIPAL...')
                break

            elif resposta == 1:
                sorteio_números()

            elif resposta == 2:
                gerador_nomes()
                
            else:
                print('\033[0;31mERRO! Digite uma opção válida.\033[m')
        return
    except resposta is float or str:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')

    except KeyboardInterrupt:
        return

def sorteio_números():
    """
    -> Pede ao usuário a quantidade de números a serem sorteados, o mínimo e o máximo. Enquanto o usuário digita, o programa valida, sendo os critérios: todos os parâmetros tem que ser números inteiros, a quantidade não pode ser menor que 1, o mínimo não pode ser menor que 0, e o máximo não pode ser menor ou igual ao número mínimo. Ao sortear, verifica se o número sorteado já saiu. Se sim, sorteia outro.
    """
    while True:
        numero = int(input('Quantos números você quer sortear? '))
        if numero < 1:
            print('\033[31mERRO! Digite um valor maior que zero.\033[m')
        else:
            break
    while True:
        min = int(input('Qual o menor número? '))
        if min < 0:
            print('\033[31mERRO! Digite um número inteiro maior que zero!\033[m')
        else:
            break
    while True:
        max = int(input('Qual o maior número? '))
        if max <= min:
            print('\033[31mERRO! Digite um número inteiro maior que o mínimo.')
        else:
            break
    sorteio = list()
    for c in range(numero):
        valor = random.randint(min, max)
        if valor not in sorteio:
            sorteio.append(valor)
        else:
            return valor
    print('Os números sorteados foram:', end=' ')
    ui.resultado(sorteio, fim=' ', linhas=False)
    sleep(2)

def gerador_nomes():
    """
    -> Pede ao usuário a quantidade de nomes a serem gerados, e gera uma lista com esses nomes.
    """
    quantidade = int(input('Digite a quantidade de nomes: '))
    nomes = list()
    from faker import Faker
    fake = Faker()
    for _ in range(quantidade):
        nome = fake.name()
        nomes.append(nome)
    ui.resultado(nomes, fim='; ')
