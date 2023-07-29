import random

class RSAEncryptor:
    def __init__(self):
        self.p = None
        self.q = None
        self.n = None
        self.totient = None
        self.e = None
        self.d = None

    def mod(self, a, b):
        if a < b:
            return a
        else:
            return a % b

    def prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_e(self, num):
        while True:
            e = random.randrange(2, num)
            if self.mdc(num, e) == 1:
                return e

    def mdc(self, n1, n2):
        rest = 1
        while n2 != 0:
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1

    def generate_prime(self):
        while True:
            x = random.randrange(1, 100)
            if self.prime(x) == True:
                return x

    def cipher(self, words):
        tam = len(words)
        i = 0
        lista = []
        while i < tam:
            letter = words[i]
            k = ord(letter)
            k = pow(k, self.e, self.n)
            d = self.mod(k, self.n)
            lista.append(str(d))
            i += 1
        return lista

    def descifra(self, cifra):
        lista = ""
        i = 0
        tamanho = len(cifra)
        while i < tamanho:
            result = pow(int(cifra[i]), self.d, self.n)
            texto = self.mod(result, self.n)
            letra = chr(texto)
            lista = lista + letra
            i += 1
        return lista

    def calculate_private_key(self, toti, e):
        d = 0
        while self.mod(d * e, toti) != 1:
            d += 1
        return d

    def generate_keys(self):
        while True:
            self.p = self.generate_prime()
            self.q = self.generate_prime()
            self.n = self.p * self.q
            self.totient = (self.p - 1) * (self.q - 1)
            self.e = self.generate_e(self.totient)
            self.d = self.calculate_private_key(self.totient, self.e)
            if self.e != self.d:  # Garantir que e e d sejam diferentes
                break
