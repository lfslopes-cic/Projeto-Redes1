import socket

HOST = '127.0.0.1' 
PORT = 50000

0
Jogadas = ['Pedra', 'Papel', 'Tesoura']


endereco = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

endereco.connect((HOST, PORT)) 

while True:
    opcao1 = int(input("\n* Escolha uma opção:\n  1 - Informar um palpite\n 0 - Para encerrar a conexão\n -> Opcao: "))

    if (opcao1 == 1):
        opcao2 = int(input("\n* Escolha o palpite:\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\n -> Opcao: "))

        if (opcao2 == 1):
            mensagemEnvioClient = 'Pedra' 
        elif (opcao2 == 2):
            mensagemEnvioClient = 'Papel' 
        elif (opcao2 == 3):
            mensagemEnvioClient = 'Tesoura' 
    
    
    if (opcao1 == 0):
        print("\nConexão encerrada!\n")
        
        endereco.close()
        break
    

    endereco.sendall(str.encode(mensagemEnvioClient)) 
    
    print("\n-> Palpite enviado pelo cliente: ", mensagemEnvioClient) 

    
    data = endereco.recv(1024) 

    print('\n*** Resultado final do jogo: \n', data.decode())
