import socket
import random


HOST = 'localhost' 
PORT = 50000


Jogadas = ['Pedra', 'Papel', 'Tesoura']
endereco= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
endereco.bind ((HOST, PORT))
endereco.listen(3)

print("Aguardando conexão de um cliente:")

conn, ender = endereco.accept() 

print('Connectado com', ender) 
print("\nOs palpites do servidor são ALEATÓRIOS!\n")

while True: 
    data = conn.recv(1024) 
   

    if not data: 
        print("\nConexão encerrada!\n")

        conn.close() 
        break
    
    palpiteClient = str(data.decode()) 
    palpiteServ = random.choice(Jogadas) 

    print("* O Servidor respondeu:", palpiteServ) 

    if ((palpiteClient == 'Tesoura' and palpiteServ == 'Papel') or (palpiteClient == 'Pedra' and palpiteServ == 'Tesoura') or (palpiteClient == 'Papel' and palpiteServ == 'Pedra')):
        ganhador = 'Cliente'
    
    if ((palpiteClient == 'Papel' and palpiteServ == 'Tesoura') or (palpiteClient == 'Tesoura' and palpiteServ == 'Pedra') or (palpiteClient == 'Pedra' and palpiteServ == 'Papel')):
        ganhador = 'Servidor'
    
    if (palpiteClient == palpiteServ):
        ganhador = 'Empate'

   
    result = '- Cliente: '+ str(palpiteClient) + '\n - Servidor: ' + str(palpiteServ) + '\n=> Vencedor: ' + str(ganhador) + '\n' # Concatenação dos resultados, sendo eles apresentados para o cliente

    conn.sendall(bytes(str(result), 'utf8'))
