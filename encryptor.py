from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted = file.read()
    decrypted = f.decrypt(encrypted)
    with open("decrypted_" + filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted)

# Run test
generate_key()
encrypt_file("secret.txt")
decrypt_file("secret.txt.enc")
