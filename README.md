# Algoritmo RSA em Python

Este é um exemplo de implementação do algoritmo RSA em Python. O algoritmo RSA é uma técnica criptográfica amplamente utilizada para a criptografia assimétrica, em que um par de chaves é gerado: uma chave pública usada para criptografar mensagens e uma chave privada usada para descriptografá-las. O algoritmo é baseado na dificuldade de fatorar grandes números primos, o que o torna seguro para comunicação segura e autenticação.

## Funcionamento

1. O servidor solicita ao usuário para fornecer dois números primos (p e q).

2. Com base nos números primos fornecidos, o servidor gera as chaves pública e privada.

3. A chave pública (n, e) é enviada ao cliente para que ele possa criptografar suas mensagens.

4. O cliente insere a mensagem a ser enviada e utiliza a chave pública para criptografá-la.

5. A mensagem criptografada é enviada de volta ao servidor.

6. O servidor, com sua chave privada, descriptografa a mensagem recebida e exibe o resultado na tela.

## Demonstração

Para executar o algoritmo, siga os seguintes passos:

1. Execute o servidor em um terminal:

```bash
python servidor.py
```

2. Em seguida, execute o cliente em outro terminal:

```bash
python cliente.py
```

## Autores

- Felipe Patriota
- Valdir Zacarias
- Matheus Chagas

