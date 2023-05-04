import threading
import time
import random

# define a função que simula a operação do caixa
def operar_caixa(nome_caixa, fila_clientes):
    tempo_total = 0
    while True:
        # espera por um cliente na fila
        if fila_clientes:
            cliente = fila_clientes.pop(0)
            print(f'{nome_caixa} chamando próximo cliente {cliente["id"]} com {cliente["itens"]} itens...')
            # processa o pagamento do cliente
            tempo_cliente = 0
            for i in range(cliente['itens']):
                time.sleep(1)
                tempo_cliente += 1
                print(f'{nome_caixa} processando item {i+1} do cliente {cliente["id"]} ({tempo_cliente}s)...')
            tempo_total += tempo_cliente
            print(f'Tempo total de processamento do cliente {cliente["id"]}: {tempo_cliente}s')
            print(f'Tempo total de processamento do {nome_caixa}: {tempo_total}s')
        else:
            # se a fila estiver vazia, espera um pouco e tenta novamente
            time.sleep(1)

# define a função observadora que monitora o número de clientes em cada fila
def observar_filas(fila_caixa1, fila_caixa2, fila_caixa3):
    while True:
        num_clientes_caixa1 = len(fila_caixa1)
        num_clientes_caixa2 = len(fila_caixa2)
        num_clientes_caixa3 = len(fila_caixa3)

        # verifica se uma das filas atingiu um limite
        if num_clientes_caixa1 >= 3:
            print(f'Fila do Caixa 1 atingiu o limite de 5 clientes (tem {num_clientes_caixa1} clientes)')
        if num_clientes_caixa2 >= 3:
            print(f'Fila do Caixa 2 atingiu o limite de 5 clientes (tem {num_clientes_caixa2} clientes)')
        if num_clientes_caixa3 >= 3:
            print(f'Fila do Caixa 3 atingiu o limite de 5 clientes (tem {num_clientes_caixa3} clientes)')

        # espera um pouco antes de verificar novamente
        time.sleep(1)

# cria as filas de clientes para cada caixa
# o random.randint está sendo utilizado para determinar a quantidade de itens e clientes de uma fila, sendo possível personalizar os valores de cada um.
fila_caixa1 = [{'id': i+1, 'itens': random.randint(1,100)} for i in range(random.randint(1, 3))]
fila_caixa2 = [{'id': i+1, 'itens': random.randint(1,100)} for i in range(random.randint(1, 3))]
fila_caixa3 = [{'id': i+1, 'itens': random.randint(1,100)} for i in range(random.randint(1, 3))]

# cria as threads para cada caixa
caixa1 = threading.Thread(target=operar_caixa, args=('Caixa 1', fila_caixa1))
caixa2 = threading.Thread(target=operar_caixa, args=('Caixa 2', fila_caixa2))
caixa3 = threading.Thread(target=operar_caixa, args=('Caixa 3', fila_caixa3))

# cria a thread observadora
observador = threading.Thread(target=observar_filas, args=(fila_caixa1, fila_caixa2, fila_caixa3))

# inicia todas as threads
observador.start()
caixa1.start()
caixa2.start()
caixa3.start()

# aguarda todas as threads finalizarem
observador.join()
caixa1.join()
caixa2.join()
caixa3.join()

print('Todos os caixas foram fechados')
