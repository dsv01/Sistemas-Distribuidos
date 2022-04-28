import socket

#==================================================================================
# Componentes da camada de interface com o usuário
#==================================================================================

def getFileName(msg):
    '''Função que implementa o componente que deve pegar o nome do arquivo
    com o texto que deve ser processado'''

    #Pegando o nome do arquivo do usuário
    fileName = input(msg)

    #Retornando o nome do arquivo passado
    return fileName

def printResult(result):
    '''Função que vai imprimir a mensagem, seja ela a lista das palavras
    (execução bem sucedida), ou uma mensagem de erro'''

    #Imprimindo a mensagem
    print(result)


#==================================================================================
# Código para construção do sistema distribuido do cliente
#==================================================================================

#Definindo a porta e host
HOST = "localhost" 
PORTA = 5000

# cria socket
sock = socket.socket()

# conecta-se com o par passivo
sock.connect((HOST, PORTA))

while True:
    #Pegando o nome do arquivo do usuário
    fileName = getFileName("Pronto para receber o nome do arquivo\n")

    #Verificando condição de parada
    if(fileName == "fim"):
        break

    # envia o nome do arquivo para o servidor
    sock.send(fileName.encode('utf-8'))

    #espera a resposta do servidor 
    result = sock.recv(1024)

    # imprime o resultado recebido
    printResult(str(result,  encoding='utf-8'))

# encerra a conexao
sock.close() 

