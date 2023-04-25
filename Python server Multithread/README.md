# Python server Multithread

### ATIVIDADE DA UNIDADE II
#### 1. Descrição da Atividade
Deverá ser desenvolvido uma aplicação cliente servidor utilizando comunicação com sockets de um serviço echo reply reverse. Exemplo: ao enviar a string “Hello World!!!” ao servidor a mensagem “!!!dlroW olleH” deve ser respondida ao cliente.

#### 2. Descrição dos Componentes que devem ser implementados

    - Módulo de comunicação com sockets TCP/IP cliente e servidor. O servidor deve suportar múltiplas conexões simultâneas.
    Utilizando programação multithread, o servidor deve atender cada requisição com uma nova thread de execução. 
    - O cliente deve suportar threads para envio em massa de requisições ao servidor (simulação de DoS).
    - Apresentar um relatório comparando tamanho (mensagens de 1byte, 512bytes, 1kb, etc) e número de requisições enviadas 
    com gráficos de utilização de CPU, memória e rede do sistema operacional do servidor.

### Relatório

#### Teste com 3 threads e com mensagens de 1024 bytes

![Captura de tela de 2023-04-25 13-12-18.png](https://github.com/Lucasx10/Sistemas-Distribuidos-2023.1/blob/main/Python%20server%20Multithread/Captura%20de%20tela%20de%202023-04-25%2013-12-18.png)

#### Gráfico gerado da utilização dos hardwares 

![2clientes.png](https://github.com/Lucasx10/Sistemas-Distribuidos-2023.1/blob/main/Python%20server%20Multithread/2clientes.png)
