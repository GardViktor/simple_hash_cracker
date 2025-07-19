import hashlib

hash_alvo = input("Hash Alvo: ")
if len(hash_alvo) == 32:
    print("Algoritmos Possiveis = md5")
elif len(hash_alvo) == 40:
    print("Algoritmos Possiveis = sha1")
elif len(hash_alvo) == 56:
    print("Algoritmos Possiveis = sha224 ou sha3_24")
elif len(hash_alvo) == 64:
    print("Algoritmos Possiveis = sha256 ou sha3_256")
elif len(hash_alvo) == 96:
    print("Algoritmos Possiveis = sha384 ou sha3_384")
elif len(hash_alvo) == 128:
    print("Algoritmos Possiveis = sha512 ou sha3_512")
else:
    print("Formato de hash desconhecido.")
    

algoritimo = input("Algoritmo (md5/sha1/sha224 ou sha3_224/sha256 ou sha3_256/sha384 ou sha3_384/sha512 ou sha3_512): ").lower()
dicionario = input("Caminho do dicionário: ")

try:

    with open(dicionario, 'r', encoding='utf-8', errors='ignore') as arquivo:
        for linha in arquivo:
            senha = linha.strip()
            
            if algoritimo == "md5":
                hash_gerado = hashlib.md5(senha.encode()).hexdigest()
            elif algoritimo == "sha1":
                hash_gerado = hashlib.sha1(senha.encode()).hexdigest()
            elif algoritimo == "sha224":
                hash_gerado = hashlib.sha224(senha.encode()).hexdigest()
            elif algoritimo == "sha3_224":
                hash_gerado = hashlib.sha3_224(senha.encode()).hexdigest()
            elif algoritimo == "sha256":
                hash_gerado = hashlib.sha256(senha.encode()).hexdigest()
            elif algoritimo == "sha256":
                hash_gerado = hashlib.sha3_256(senha.encode()).hexdigest()
            else:
                print("Algoritimo Não Encontrado")
                break

            if hash_gerado == hash_alvo:
                print(f"Senha Encontrada {senha}")
                break

        else:
            print("Senha Não Encontrada no Dicionario")
except FileNotFoundError:
    print("Arquivo de Dicionario não encontrao!")

    

        