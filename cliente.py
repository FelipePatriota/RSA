import socket
from rsa_encryptor import RSAEncryptor

def criandoCliente():
    HOST = socket.gethostname()
    PORT = 5010  # Mesma porta utilizada pelo servidor

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    cliente.connect(dest)

    data = cliente.recv(1024).decode().split(" ")
    print("Você recebeu a chave pública do servidor: n =", data[0], "e =", data[1])

    rsa = RSAEncryptor()
    rsa.n = int(data[0])
    rsa.e = int(data[1])

    print('Para sair, use 0\n')
    msg = ''
    while msg != '0':
        msg = input("Digite uma nova mensagem:")
        cript = rsa.cipher(msg)
        cript_str = " ".join(cript)
        cliente.send(cript_str.encode())
        print("Seu texto criptografado é:", cript)
    cliente.close()

criandoCliente()
