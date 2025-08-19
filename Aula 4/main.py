from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import ast

private_key = None
public_key = None


def generate_keys() -> None:
    global private_key, public_key

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    
    print(f"\n[+] Novas chaves geradas.")


def encode_message():
    global encrypted_message

    opc_public_key = input(f"\nInsira a chave pública para criptografia. [Enter para usar a criada] ")
    if opc_public_key == "":
        if not public_key:
            print("[!] Chave pública não encontrada. Tente gerar novamente!")
            return
        else:
            opc_public_key = public_key

    original_text = str(input("Digite a mensagem para encriptar: "))
    print(f"O texto original é: '{original_text}'")

    message_bytes = original_text.encode('utf-8')

    encrypted_message = opc_public_key.encrypt(
        message_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print("\nO texto encriptado (em bytes) é:")
    print(encrypted_message)


def decode_message():
    if not private_key:
        print("\n[!] Chave privada não encontrada. Tente gerar novamente!")
        return
    
    encrypted_message_str = input("\nInsira a mensagem encriptada (em bytes): ")
    encrypted_message = ast.literal_eval(encrypted_message_str)

    print("\nDecriptando a mensagem...")
    
    decrypted_bytes = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    decrypted_text = decrypted_bytes.decode('utf-8')
    print(f"O texto decriptado é: '{decrypted_text}'")


def main() -> None:
    while True:
        print("\n" + "-" * 24)
        print(f"Criptografia RSA")
        print("-" * 24)
        print("Escolhe uma opção para prosseguir:")
        print("\t[1] Gerar novas chaves")
        print("\t[2] Encriptar uma mensagem")
        print("\t[3] Decriptar uma mensagem")
        print("\t[Qualquer outra tecla] Sair")
        opc = str(input("=>  "))
        print("-" * 24)

        if opc == "1":
            generate_keys()
        elif opc == "2":
            encode_message()
        elif opc == "3":
            decode_message()
        else:
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
    print("")