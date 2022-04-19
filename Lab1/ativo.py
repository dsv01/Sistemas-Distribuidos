#Lado ativo, que vai  enviar capturar as mensagem a serem ecoadas

from ast import While
import socket

HOST = "localhost" 
PORTA = 5000

# cria socket
sock = socket.socket()

# conecta-se com o par passivo
sock.connect((HOST, PORTA))

# # envia uma mensagem a ser ecoada
# msg = input()
# sock.send(msg.encode('utf-8'))

# #espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
# echo = sock.recv(1024)

# # imprime a mensagem recebida
# print(str(echo,  encoding='utf-8'))

while True:
    #Capturando a mensagem e verificando se corresponde a mensagem para terminar o eco que e
    #encerrar eco
    msg = input()
    if(msg == "encerrar eco"):
        break

    # envia uma mensagem a ser ecoada
    sock.send(msg.encode('utf-8'))

    #espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
    echo = sock.recv(1024)

    # imprime a mensagem recebida
    print(str(echo,  encoding='utf-8'))

# encerra a conexao
sock.close() 

