# Atividade 1

### Objetivo
Implementação de um chat cliente e servidor TCP em Python, com suporte a multiusuários e com um recurso de segurança, criptografia na comunicação aos programas cliente e servidor para garantir a confidencialidade das informações
trocadas com a biblioteca base64.

### Imports utilizados
    sys
    socket
    base64
    threading

### Teste da comunicação
![teste_chat.png](https://github.com/Lucasx10/Sistemas-Distribuidos-2023.1/blob/main/ClienteServidorPython/chat/teste_chat.png)

#### Utilizado o comando 
      sudo tcpdump -i any 'port 5000'
Para capturar e analisar pacotes de outras comunicações na rede
