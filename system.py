# Importações
from time import sleep
import lib.ui

lib.ui.cabeçalho('Sistema Python')
opções = (
    'Sair',
    'Conversor',
    'Jogos',
    'Sorteador',
    'Gerador de Senhas'
)

while True:
    print('Escolha uma das opções abaixo:')
    lib.ui.menu(opções, título=False)

    try:
        escolha = int(input('Escolha: '))
        if escolha < 0 or escolha >= len(opções):
            print('\033[31mOpção inválida. Tente novamente.\033[m')
            sleep(1)
            continue
    except ValueError:
        print('\033[31mDigite um número inteiro válido.\033[m')
        sleep(1)
        continue

    try:
        if escolha == 0:
            lib.ui.cabeçalho('Saindo do sistema... Até logo!')
            sleep(.5)
            break

        elif escolha == 1:
            sleep(.25)
            import lib.conversor_unidades
            sleep(.25)
            lib.conversor_unidades.conversor()

        elif escolha == 2:
            sleep(.25)
            import lib.jogos
            sleep(.25)
            lib.jogos.jogos()

        elif escolha == 3:
            sleep(.25)
            import lib.sorteador
            sleep(.25)
            lib.sorteador.sorteio()

        elif escolha == 4:
            sleep(.25)
            import lib.passwords_generator
            sleep(.25)
            lib.passwords_generator.sorteio()

        sleep(2)

    except Exception as e:
        print(f'\033[31mErro: {e}\033[m')
        sleep(2)
        continue
