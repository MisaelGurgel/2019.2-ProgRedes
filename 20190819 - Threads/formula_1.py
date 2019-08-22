import threading
import time

quantidade_voltas = 5

def carro_f1(nome_piloto, velocidade_carro):
    contador_voltas = 0
    while contador_voltas <= quantidade_voltas:
        time.sleep(velocidade_carro)
        print('PILOTO: {0} ....... VOLTA {1}'.format(nome_piloto, contador_voltas))
        print(threading.enumerate())
        print(threading.current_thread())
        print('')
        contador_voltas += 1
        time.sleep(1)

try:
    #carro_f1('Lewis Hamilton', 5)
    piloto_1 = threading.Thread(target=carro_f1, args=('Lewis Hamilton', 5, ), name='p1')
    piloto_1.start()

    #carro_f1('Sebastian Vettel', 4)
    piloto_2 = threading.Thread(target=carro_f1, args=('Sebastian Vettel', 3, ), name='p2')
    piloto_2.start()

    #carro_f1('Max Verstappen', 2)
    piloto_3 = threading.Thread(target=carro_f1, args=('Max Verstappen', 5, ), name='p3')
    piloto_3.start()

    #carro_f1('Kimi Raikkonen', 3)
    piloto_4 = threading.Thread(target=carro_f1, args=('Kimi Raikkonen', 2, ), name='p4')
    piloto_4.start()
except:
    print('ERRO: A corrida não pode ser iniciada...')


