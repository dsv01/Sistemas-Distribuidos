import collections
import socket
import select 
import sys  
import threading

#Definindo a porta e host
HOST = ''    
PORT = 5000  

#define a lista de I/O de interesse (jah inclui a entrada padrao)
entradas = [sys.stdin]

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

def iniciaServidor():
	'''Cria um socket de servidor e o coloca em modo de espera por conexoes
	Saida: o socket criado'''
	# cria o socket 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet( IPv4 + TCP) 

	# vincula a localizacao do servidor
	sock.bind((HOST, PORT))

	# coloca-se em modo de espera por conexoes
	sock.listen(5) 

	# configura o socket para o modo nao-bloqueante
	sock.setblocking(False)

	# inclui o socket principal na lista de entradas de interesse
	entradas.append(sock)

	return sock

def aceitaConexao(sock):
	'''Aceita o pedido de conexao de um cliente
	Entrada: o socket do servidor
	Saida: o novo socket da conexao e o endereco do cliente'''

	# estabelece conexao com o proximo cliente
	clisock, endr = sock.accept()

	return clisock, endr


def atendeRequisicoes(clisock, endr):
	'''Recebe mensagens e as envia de volta para o cliente (ate o cliente finalizar)
	Entrada: socket da conexao e endereco do cliente
	Saida: '''

	while True:
		#Pegando nome do arquivo solicitado
		fileName = str(clisock.recv(1024),encoding='utf-8')

		#Verificando se arquivo encerrou
		if(not fileName):
			print(str(endr) + '-> encerrou')
			clisock.close()
			return 

		#Processando resultado
		result = process(checkFile(fileName))

		#Devolvendo mensagem
		clisock.send(str(result).encode('utf-8'))
	


def main():
	'''Inicializa e implementa o loop principal (infinito) do servidor'''
	clientes=[] #armazena as threads criadas para fazer join
	sock = iniciaServidor()
	print("Pronto para receber conexoes...")
	while True:
		#espera por qualquer entrada de interesse
		leitura, escrita, excecao = select.select(entradas, [], [])
		#tratar todas as entradas prontas
		for pronto in leitura:
			if pronto == sock:  #pedido novo de conexao
				clisock, endr = aceitaConexao(sock)
				print ('Conectado com: ', endr)
				#cria nova thread para atender o cliente
				cliente = threading.Thread(target=atendeRequisicoes, args=(clisock,endr))
				cliente.start()
				clientes.append(cliente) #armazena a referencia da thread para usar com join()
			elif pronto == sys.stdin: #entrada padrao
				cmd = input()
				if cmd == 'fim': #solicitacao de finalizacao do servidor
					for c in clientes: #aguarda todas as threads terminarem
						c.join()
					sock.close()
					sys.exit()


main()