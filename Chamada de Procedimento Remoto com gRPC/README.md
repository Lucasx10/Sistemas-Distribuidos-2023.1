# Atividade: Criando uma aplicação de controle remoto com gRPC

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


## Testes
    
