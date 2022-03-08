import time
from cryptography.fernet import Fernet

key = Fernet.generate_key()   ##Key Generation

t=Fernet(key)  ## Symmetric Key 

message="Hello! how are you?" ## Message to encrypt

cipher=t.encrypt(message.encode())  ##Encodes to bytes inorder to encrypt

print("\n++++++++++++++++  Encryption ++++++++++++++++\n")
print(cipher.decode())

time.sleep(3)
print("\n++++++++++++++++  Decryption ++++++++++++++++\n")
print(t.decrypt(cipher).decode(),"\n")

