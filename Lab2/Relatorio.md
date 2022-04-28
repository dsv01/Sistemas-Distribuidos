# Relatório do Lab 2

Para construir a aplicação do sistema distribuido que vai receber, ler e contar a quantidade de palavras em um arquivo e avaliar as 5 palavras mais frequentes vamos construir uma arquitetura de software em camadas. E depois vamos organizar os componentes em uma estrutura cliente-servidor na arquitetura de sistema. Depois vamos implementar o código com base nessas especificações. Trabalhamos essas construções nos tópicos seguintes.

## Atividade 1 Arquitetura de software

A arquitetura será desenvolvida em três camadas, a de interface com o usuário, a de processamento, e a de acesso aos dados. Criaremos os componentes em cada uma delas da seguinte forma.

### Interface com o usuario

``getFileName``
Componente que vai pegar o nome do arquivo do usuário.

``printResult`` 
Componente que vai retornar a lista das palavras, ou mensagem de erro.

### Processamento

``Process`` 
Componente que recebe o conteúdo, faz a contagem das palavras, e retorna o resultado para a camada de interface com o usuário

### Acesso aos dados

``checkFile``
Componente que verifica a existencia do arquivo solicitado e envia o conteudo dele para a camada de processamento

## Atividade 2 Arquitetura de sistema

A arquitetura será de dois níveis, do tipo cliente-servidor.Vamos separar para o lado cliente os componentes da camada de interface com o usuário da arquitetura de software definida no item anterior. E vamos separar os componentes do processamento e acesso aos dados para o lado do servidor. 

### Cliente

``getFileName``
``printResult``

### Servidor

``Process``
``checkFile``

## Atividade 3 Implementação do sistema distribuido

Com base nas arquiteturas construidas nos itens 1 e 2, podemos montar o código nesse diretório como uma parte como cliente, e outra como servidor. O cliente espera receber um nome de arquivo txt presente nesse diretório, caso não receba ele vai exibir uma mensagem de erro. Portanto para executar é preciso editar um dos arquivos e chamar pelo nome dele, ou criar um e chamar pelo seu nome no cliente.