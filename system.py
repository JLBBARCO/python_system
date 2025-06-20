# Importações
from time import sleep
import lib.interface

lib.interface.cabeçalho('Sistema Python')
while True:
    print('Escolha uma das opções abaixo:')
    opções = (
        'Sair',
        )
    lib.interface.menu(opções, título=False)

    escolha = int(input('Escolha: '))
    while escolha < 0 or escolha > len(opções):
        escolha = int(input('Escolha: '))

    if escolha == 0:
        lib.interface.cabeçalho('Saindo do sistema... Até logo!')
        sleep(.5)
        break

    else:
        print('\033[31mOpção inválida. Tente novamente.\033[m')
        # Aqui você pode adicionar o código para lidar com a opção inválida
    sleep(2)
