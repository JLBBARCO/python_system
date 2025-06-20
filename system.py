# Importações
from time import sleep
import lib.interface

lib.interface.cabeçalho('Sistema Python')
while True:
    print('Escolha uma das opções abaixo:')
    opções = (
        'Sair',
        'Conversor',
        'Downloads',
        )
    lib.interface.menu(opções, título=False)

    escolha = int(input('Escolha: '))
    while escolha < 0 or escolha > len(opções):
        escolha = int(input('Escolha: '))

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

        else:
            print('\033[31mOpção inválida. Tente novamente.\033[m')
            # Aqui você pode adicionar o código para lidar com a opção inválida
        sleep(2)

    except Exception as e:
        print(f'\033[31mErro: {e}\033[m')
        sleep(2)
        continue