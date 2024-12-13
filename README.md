# Projeto de Redes I, do curso Ciência da Computação da UESC - Universidade Estadual de Santa Cruz
    
    Projeto de Redes I, feito por Luiz Felipe Santos e Luciana Roncarati I.
    
# Projeto de jogo: Pedra, Papel e Tesoura

    Projeto feito em Python utilizando as bibliotecas Socket do Python, utilizando o Host padrão e porta 50000 para conexão. O projeto foi criado em duas etapas. 
    A primeira:
    
# client.py
       
        - Nele temos uma conexão TCP/IP para não ter perda de pacotes;
        - O usuário seleciona 1, 2 ou 3 para selecionar "Pedra","Papel" ou "Tesoura", e a função sendall envia a opção selecionada pelo cliente para o servidor;
        - O cliente recebe do Servidor através da função recv a opção do seu adversário e quem ganhou dos dois, ou, caso eles empatem, o cliente recebe a mensagem de empate;
        - O cliente também uma resposta do Servidor, indicando a desconexão do servidor, para assim encerrar a conexão do cliente.

    Depois temos a segunda etapa:
    
# server.py
        
        - Nele também temos uma conexão TCP/IP e o Host é o localhost;
        - O servidor recebe a conexão de dois clientes, que enviam suas opções entre pedra, papel e tesoura;
        - Na função servidor temos as regras do jogo (Tesoura vence Papel, Papel vence Pedra e Pedra vence Tesoura);
        - De acordo com as regras temos o ganhador e enviado para o cliente que visualiza na tela o resultado.

        
