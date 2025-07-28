from cryptography.fernet import Fernet, MultiFernet

message = 'Secret message'.encode()

key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())

f = MultiFernet([key1, key2])
token = f.encrypt(message)

message_decrypted = f.decrypt(token)

print(token)
print()
print(message_decrypted)