# Importações
from time import sleep
import lib.interface

lib.interface.cabeçalho('Sistema Python')
opções = (
    'Sair',
    'Conversor',
    'Downloads',
    'IA (Inteligência Artificial)',
    'Jogos',
    'Sorteador'
)

while True:
    print('Escolha uma das opções abaixo:')
    lib.interface.menu(opções, título=False)

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
            lib.interface.cabeçalho('Saindo do sistema... Até logo!')
            sleep(.5)
            break

        elif escolha == 1:
            sleep(.25)
            import lib.conversor_unidades
            sleep(.25)
            lib.conversor_unidades.conversor()

        elif escolha == 2:
            import lib.downloads
            lib.downloads.yt_download()

        elif escolha == 3:
            import lib.ia

        elif escolha == 4:
            sleep(.25)
            import lib.jogos
            sleep(.25)
            lib.jogos.jogos()

        elif escolha == 5:
            sleep(.25)
            import lib.sorteio
            sleep(.25)
            lib.sorteio.sorteio()

        sleep(2)

    except Exception as e:
        print(f'\033[31mErro: {e}\033[m')
        sleep(2)
        continue