import hashlib, hmac  # apenas o necessário

print("\nItem A) ------------------------------")
mensagem = "Mensagem de Teste"

def gerar_hash(mensagem: str) -> str:
    return hashlib.sha256(mensagem.encode()).hexdigest()

def verificar_hash(mensagem_original: str, mensagem_codificada: str) -> bool:
    if gerar_hash(mensagem_original) == mensagem_codificada:
        print(f"TRUE - A mensagem `{mensagem_original}` está OK!")
        return True
    print(f"FALSE - A mensagem `{mensagem_original}` está errada!")
    return False

mensagem_hash = gerar_hash(mensagem)
verificar_hash("Mensagem de Teste", mensagem_hash)

# ===== Parte 2: Hash com chave (HMAC) =====
print("\nItem B) ------------------------------")

# chave = b"chave_secreta"
# hmac_msg = hmac.new(chave, mensagem.encode(), hashlib.sha256).hexdigest()

# print("\nMensagem:", mensagem)
# print("HMAC:", hmac_msg)

# Verificando integridade + autenticidade
# recebida = "Segurança de Sistemas - Aula 03"
# print("Integridade+Autenticidade OK?", hmac.new(chave, recebida.encode(), hashlib.sha256).hexdigest() == hmac_msg)

print("")