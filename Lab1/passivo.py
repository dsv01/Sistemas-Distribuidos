# Lado passivo da aplicação (servidor de echo)

import socket

HOST = ''    
PORTA = 5000  

# cria um socket para comunicacao
sock = socket.socket() 

# vincula a interface e porta para comunicacao
sock.bind((HOST, PORTA))

# define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
sock.listen(5) 

# aceita a primeira conexao da fila (chamada pode ser BLOQUEANTE)
novoSock, endereco = sock.accept() 

#Verificando a mensagem para realizar o echo
while True:
    msg = novoSock.recv(1024)
    if(not msg):
        break
    else:
        #Devolvendo mensagem
        novoSock.send(msg)


# fecha o socket da conexao
novoSock.close() 

# fecha o socket principal
sock.close() 