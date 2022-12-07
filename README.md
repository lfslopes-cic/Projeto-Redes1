# Projeto de jogo: Pedra, Papel e Tesoura

    Projeto feito em Python utilizando as bibliotecas Socket e Random do Python, utilizando o Host padrão e porta 50000 para conexão. O projeto foi criado em duas           etapas. 
    A primeira:
    
# client.py
       
        - Nele temos uma conexão TCP/IP para não ter perda de pacotes;
        - Tem 3 variaveis ("Pedra","Papel", "Tesoura"), onde o usuário seleciona uma das três e a função sendall é como um send, ou seja, ele envia a opção selecionada
          pelo cliente para o servidor;
        - E tem a função recv para receber o resultado do servidor.

    Depois temos a segunda etapa:
    
# server.py
        
        - Nele também temos uma conexão TCP/IP e host é um localhost;
        - Também tem as 3 variaveis ("Pedra","Papel", "Tesoura"), onde o servidor entra com uma variavel aleatória e envia o resultado para o cliente 
          onde temos uma limitação de interações;
        - Limitados a 1024 bytes;
        - Na função servidor temos as regras do jogo (Tesoura vence Papel, Papel vence Pedra e Pedra vence Tesoura);
        - De acordo com as regras temos o ganhador e enviado para o cliente que visualiza na tela o resultado.

        
