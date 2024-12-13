import socket


HOST = 'localhost'
PORT = 50000

Jogadas = ['Pedra', 'Papel', 'Tesoura']

#   Criando um novo socket com a família de endereço padrão, que é especificado pelo protocolo IPv4 e
#   utilizando o protocolo de transporte TCP.
endereco = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Conectando cliente ao endereço 127.0.0.1 e a porta 50000
endereco.connect((HOST, PORT))
resposta = '1'
while resposta != b'0':
    opcao = int(input("\n* Escolha uma opção:\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\n -> Opcao:\n"))
    if opcao == 1:
        mensagemEnvioClient = 'Pedra'
    elif opcao == 2:
        mensagemEnvioClient = 'Papel'
    elif opcao == 3:
        mensagemEnvioClient = 'Tesoura'
    else:
        mensagemEnvioClient = None
        print("Opcao invalida")

    if mensagemEnvioClient is None:
        print("Desconectando...")
        break
    endereco.sendall(str.encode(mensagemEnvioClient))
    print("\n-> Palpite enviado pelo cliente: ", mensagemEnvioClient)
    opcaoAdversario = endereco.recv(1024)
    print("-> Palpite enviado pelo adversario: ", opcaoAdversario.decode())
    mensagemResultado = endereco.recv(1024)
    print(mensagemResultado.decode())

    resposta = endereco.recv(1024)

print("\nConexão encerrada!\n")
        
endereco.close()