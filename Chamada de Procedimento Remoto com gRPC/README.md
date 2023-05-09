# Atividade 4: Criando uma aplicação de controle remoto com gRPC

### Objetivo
O objetivo é permitir que o cliente envie comandos em formato de string para o servidor, que irá executar esses comandos em uma máquina Linux e retornar o resultado para o cliente.

### Descrição
A aplicação é composta por um servidor e um cliente, implementados usando gRPC e Python. O servidor foi configurado para receber comandos em formato de string do cliente e executá-los em uma máquina Linux. O cliente permite que o usuário insira os comandos que deseja executar e exibe o resultado da execução.

### Ferramentas
    Biblioteca (subprocess) para executar comandos bash no servidor;
    Biblioteca (grpc) para implementar a comunicação entre o cliente e o servidor;
    Biblioteca (click) para implementar a interface de linha de comando do cliente;
    
### Bonus 
- Foi implementado um sistema de logs para armazenar as informações de execução do cliente;

### Execução
    python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. my_service.proto
    python3 server_grpc.py
    python3 cliente_grpc.py
    
## Testes
Teste de comandos do cliente
![teste_comandos.png](https://github.com/Lucasx10/Sistemas-Distribuidos-2023.1/blob/main/Chamada%20de%20Procedimento%20Remoto%20com%20gRPC/teste_comandos.png)

Teste de gravação dos logs do comando 
![teste_log.png](https://github.com/Lucasx10/Sistemas-Distribuidos-2023.1/blob/main/Chamada%20de%20Procedimento%20Remoto%20com%20gRPC/teste_log.png)
