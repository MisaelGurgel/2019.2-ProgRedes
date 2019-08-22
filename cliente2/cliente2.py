import socket
HOST = '10.25.2.17' #Falta definir o ip do servidor     10.25.2.21 ip da maquina
PORT = 5565 # porta do server


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST, PORT))
nomeArquivo = input("Nome do Arquivo")
fd = open (nomeArquivo, "r")
nomeArquivo = nomeArquivo.encode('utf-8')
tcp_socket.send(nomeArquivo)
while True:
    
    msg = input('Digite a mensagem: ')

    msg = msg.encode('utf-8')

    tcp_socket.send(msg)

    if not msg: break

tcp_socket.close()


