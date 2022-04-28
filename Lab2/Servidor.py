import collections
import socket

#==================================================================================
# Componentes da camada de processamento
#==================================================================================


def process(file):
    '''Função para ler, verificar, e fazer a contagem das palavras do conteudo do arquivo'''

    #Verificando arquivo
    if(file == "Arquivo inexistente"):
        return file

    #Formatando como uma lista de palavras
    fileContent = []
    for line in file:
        fileContent = fileContent + line.split(" ")

    #Realizando o processamento do texto
    result = collections.Counter(fileContent)

    #Fechando arquivo
    file.close()

    #Retornando o resultado do processamento
    sortedList = sorted(list(result.items()),key = lambda x : x[1],reverse=True)
    return sortedList[0:5]


#==================================================================================
# Componentes da camada de acesso aos dados
#==================================================================================

def checkFile(fileName):
    '''Função para verificar se arquivo existe'''

    #Verificando se o arquivo existe 
    try:
        return open(fileName + ".txt",'r')
    except:
        return "Arquivo inexistente"


#==================================================================================
# Código para construção do sistema distribuido do servidor
#==================================================================================

#Definindo a porta e host
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

#Verificando e processando arquivo solicitado pelo cliente
while True:
    #Pegando nome do arquivo solicitado
    fileName = str(novoSock.recv(1024),encoding='utf-8')

    #Processando resultado
    result = process(checkFile(fileName))

    #Devolvendo mensagem
    novoSock.send(str(result).encode('utf-8'))


# fecha o socket da conexao
novoSock.close() 

# fecha o socket principal
sock.close() 