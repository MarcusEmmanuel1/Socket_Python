import socket
import random
import string


# Função de contagem de digitos
def digitCount(n):
    return len(str(n))


# Função para gerar uma string aleatória.
def randomStringGenerator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Função de checagem de número par
def evenNumber(n):
    if n % 2 == 0:
        return True

    return False


HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen()
    print('Aguardando conexão...')
    conn, ender = s.accept()
    print('Conectado no endereço: ', ender)

    while True:
        data = conn.recv(1024)
        if not data:
            print('Encerrando conexão.')
            conn.close()
            print("*********************")
            break
        if digitCount(abs(int(data))) > 10:
            data = randomStringGenerator(digitCount(abs(int(data)))).encode()
        elif digitCount(abs(int(data))) <= 10:
            r = evenNumber(int(data))
            if r:
                data = b'PAR'
            else:
                data = 'ÍMPAR'.encode('utf-8') #O UTF-8 SERVE PARA UMA MAIOR REPRESENTAÇÃO DE CARACTERES
        conn.sendall(data)
