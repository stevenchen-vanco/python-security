import hashlib

def md5(msg):
    return print(hashlib.md5(msg).hexdigest(),"MD5")
    
def sha1(msg):
    return print(hashlib.sha1(msg).hexdigest(),"SHA1")
    
def sha128(msg):
    return print(hashlib.sha128(msg).hexdigest(),"SHA128")

def sha256(msg):
    return print(hashlib.sha256(msg).hexdigest(),"SHA256")

def sha512(msg):
    return print(hashlib.sha512(msg).hexdigest(),"SHA512")


def main():

    message=input("Enter your message to generate hash:\t")
    opt=int(input("Main Menu\n\n1.md5\n\n2.sha1\n\n3.sha128\n\n4.sha256\n\n5.sha512\n\noption:\t"))
    msg=message.encode()

    if opt == 1:
        md5(msg)
    elif opt == 2:
        sha1(msg)
    elif opt == 3:
        sha128(msg)
    elif opt == 4:
        sha256(msg)
    elif opt == 5:
        sha512(msg)
    else:
        sys.exit("\n\nEnter a valid option...")

main()

