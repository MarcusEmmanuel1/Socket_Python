import socket
import time
import random

#Funções utilitárias
def randomNumberGenerator():
    # Gerando um número inteiro aleatório de até 30 casas
    num_casas = random.randrange(1, 31)  # número aleatório de 1 a 30
    num = random.randint(10 ** (num_casas - 1),
                         (10 ** num_casas) - 1)  # Número aleatório com o número de casas especificado
    return num

HOST = 'localhost'
PORT = 50000

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    num = randomNumberGenerator()
    print(f'CLIENTE:  {num}')

    # Convertendo o número para bytes e enviando ao servidor
    s.send(str(num).encode())

    # Recebendo a resposta do servidor e convertendo de volta para inteiro
    data = s.recv(2048)
    response = data.decode()

    # Imprimindo o valor recebido e a mensagem "FIM"
    print(f'SERVIDOR: {response} FIM')

    # Encerrando a conexão
    s.close()
    print("***********************************************")
    # Esperando 10 segundos antes de iniciar a próxima iteração
    time.sleep(10)
