import socket

HOST = '0.0.0.0' #    IP padrão para receber conexões
PORT = 50000


Jogadas = ['Pedra', 'Papel', 'Tesoura']
endereco= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
endereco.bind ((HOST, PORT))
endereco.listen(2)

print("Aguardando conexão de um cliente:", endereco.getsockname())

conn, ender = endereco.accept()
print('Conectado com', ender)
conn2, ender2 = endereco.accept()
print("Conectado com", ender2)


data = conn.recv(1024)
data2 = conn2.recv(1024)

if not data or not data2:
    print("\nConexão encerrada!\n")
    conn.close()
    conn2.close()
    
palpiteClient = str(data.decode())
palpiteClient2 = str(data2.decode())

conn.send(palpiteClient2.encode())
conn2.send(palpiteClient.encode())

if ((palpiteClient == 'Tesoura' and palpiteClient2 == 'Papel') or
        (palpiteClient == 'Pedra' and palpiteClient2 == 'Tesoura') or
        (palpiteClient == 'Papel' and palpiteClient2 == 'Pedra')):
        ganhador = 'Cliente 1'
        conn.send("---      Você é o vencedor!      ---".encode())
        conn2.send("---         você perdeu!        ---".encode())
    
if ((palpiteClient == 'Papel' and palpiteClient2 == 'Tesoura') or
        (palpiteClient == 'Tesoura' and palpiteClient2 == 'Pedra') or
        (palpiteClient == 'Pedra' and palpiteClient2 == 'Papel')):
        ganhador = 'Cliente 2'
        conn2.send("---     Voce é o vencedor!      ---".encode())
        conn.send("---          você perdeu!     ---".encode())
    
if (palpiteClient == palpiteClient2):
    ganhador = '---     Empate!     ---'
    conn.send(ganhador.encode())
    conn2.send(ganhador.encode())

if ganhador == "---     Empate!     ---":
    result = "Os clientes empataram!"
else:
    result = '- Cliente 1: '+ str(palpiteClient) + '\n- Cliente 2: ' + str(palpiteClient2) + '\n=> Vencedor: ' + str(ganhador) + '\n' # Concatenação dos resultados, sendo eles apresentados para o cliente

resultEntregado = '0'

print (result)
conn.send(resultEntregado.encode("UTF-8"))
conn2.send(resultEntregado.encode("UTF-8"))
conn.close()
conn2.close()
