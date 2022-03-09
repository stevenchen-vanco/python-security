import time
import sys
import base64
from cryptography.fernet import Fernet

def key_generation(message):
    key = Fernet.generate_key()   ##Key Generation
    fernet=Fernet(key)
    return fernet 

def encrypt():
    message = input("Enter your message to encrypt: ")
    path = input("Enter a file to store symmetric key:(/root/enc.txt) ")
    if not message or not path:
        sys.exit("No message/path provided..")

    encrypt=key_generation(message).encrypt(message.encode())
    print(encrypt)
    try:
        with open(path,"wb") as file:
            file.write(encrypt)
    except:
        sys.exit("Check your filename and file permissions")
    
    
def main():
    opt=int(input("Main Menu\n1.Encrypt.\n2.Decrypt\n0.Exit."))
    if opt == 1:
        encrypt()
    elif opt == 2:
        sys.exit("Will be added on next update") #decrypt()
    elif opt == 0:
        quit()
    else:
        sys.exit("Kindly select a valid option...")

main()