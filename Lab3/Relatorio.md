# Relatório do Lab 3

Neste laboratório vamos estender a aplicação do laboratório 2 para que ele funcione com um servidor concorrente. Mantendo toda as demais estruturações da aplicação do laboratório 2. 

## Atividade 1 Reprojetando Implementação do Servidor

Nessa atividade vamos projetar como alterar o servidor para que ele possa receber comandos básicos da entrada padrão, e posteriormente como torná-lo um servidor concorrente

### Projeto para Entrada Padrão

Para podermos reagir as requisições da entrada padrão vamos detectar as novas requisições utilizando a função select, e vamos armazenar essas entradas usando uma lista global.

### Projeto para Servidor Concorrente

Para criarmos um novo fluxo para cada cliente utilizamos o módulo do python threading, que vai nos permitir isso. Como estamos apenas lendo o arquivo não precisamos nos procupar com condições de corrida.


## Atividade 2 Implementação da extensão

Tendo definido os pontos a se estender implementamos a extensão descrita na atividade 1 nos arquivos Cliente.py e Servidor.py neste diretório.  
