import socket
from rsa_encryptor import RSAEncryptor

def criandoServidor(n, e, d):
    HOST = socket.gethostname()
    PORT = 5010
    servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    servidor_tcp.bind(orig)
    servidor_tcp.listen(1)
    con, cliente = servidor_tcp.accept()
    print('Conectado por:', cliente)
    con.send((str(n) + " " + str(e)).encode())
    msg = ''
    print("Aguardando dados do cliente:")
    while msg != '0':
        msg = con.recv(1024).decode()
        msg = rsa.descifra(msg.split(" "))
        if not msg:
            break
        print(cliente, msg)
    print('Finalizando conexão do cliente', cliente)
    con.close()

print("-------------------Bem vindo----------------")
p = int(input("Digite um valor para P:"))
q = int(input("Digite um valor para Q:"))

rsa = RSAEncryptor(p, q)

public_key = (rsa.n, rsa.e)
private_key = rsa.d

print("Sua chave pública é:", public_key)
print("Sua chave privada é:", private_key)

criandoServidor(rsa.n, rsa.e, rsa.d)
