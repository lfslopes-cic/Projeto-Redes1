# Projeto de jogo pedra papel e tesoura
    projeto feito em python utilizando as bibliotecas Soctet e Radon do python 
    utilizando o Host padrão e porta 50000 para conexão

    o projeto foi craido em duas etapas o primeiro:
# client.py
       
        Nele temos uma conexão tcp/ip para não ter perda de pacotes 
        tem 3 variaveis ("Pedra","Papel", "Tesoura")
        Onde o usuario ele seleciona uma das tres e a função sendall é como send ou seja ele envia o que o usario coloclou para o servidor]
        e tem a função recv para receber o resultado do servidor

    a segunda etapa:
# server.py
        
        Nele temos uma conexão tcp/ip para não ter perda de pacotes 
        e host é um localhost
        tem 3 variaveis ("Pedra","Papel", "Tesoura")
        Onde o servidor entra com uma variavel aleatoria e envia o resultado para o cliente 
        onde temos uma limitação de interações 
        e tambem libitados a 1024 bytes
        na função servidor temos as regras do jogo 
        e de acordo com as regras temos o ganhador e enviado para o cliente que visualiza na tela 

        