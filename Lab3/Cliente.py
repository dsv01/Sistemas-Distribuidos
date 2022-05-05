import socket

#Definindo a porta e host
HOST = "localhost" 
PORT = 5000

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

def iniciaCliente():
	'''Cria um socket de cliente e conecta-se ao servidor.
	Saida: socket criado'''
	# cria socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet (IPv4 + TCP) 

	# conecta-se com o servidor
	sock.connect((HOST, PORT)) 

	return sock

def fazRequisicoes(sock):
    '''Faz requisicoes ao servidor e exibe o resultado.
    Entrada: socket conectado ao servidor'''
    while True:
        #Pegando o nome do arquivo do usuário
        fileName = getFileName("Pronto para receber o nome do arquivo\n")

        #Verificando condição de parada
        if (fileName == 'fim'):
            break 

        # envia o nome do arquivo para o servidor
        sock.send(fileName.encode('utf-8'))

        #espera a resposta do servidor 
        result = sock.recv(1024)
    
        # imprime o resultado recebido
        printResult(str(result,  encoding='utf-8'))

    # encerra a conexao
    sock.close()


def main():
	'''Funcao principal do cliente'''
	#inicia o cliente
	sock = iniciaCliente()
	#interage com o servidor ate encerrar
	fazRequisicoes(sock)

main()

