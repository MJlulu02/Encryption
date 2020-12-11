# Character encoding from 32 to 126
def CodePoint():
    for i in range(32,127):
        print(chr(i), end=' ')

# Numbering Message
def Encryption():
    # To decrypt, simply put the message encrypt and set the offset to negative.

    msg = input("Veuillez indiquer un message à chiffrer")
    decalage = input("Veuillez indiquer un décalage")

    print(Encrypter(msg, decalage))

# Auto Encryption Detection
def Decrypter():
    encryptedMessage = input("Veuillez indiquer un message Chiffrer")

    for i in range(32,127):
        result = Encrypter(encryptedMessage, (32-i))
        if(' ' in result and result[0].isupper()):
            print(i, result)

# Dependances
def Encrypter(msg, decalage):
    encryptedMessage = ""

    for c in msg:
        encryptedChar = NormalizeChar(ord(c) + int(decalage))
        encryptedMessage += chr(encryptedChar)

    return encryptedMessage

def NormalizeChar(asciiIndex):
    if asciiIndex > 126:
        return asciiIndex%125
    elif asciiIndex < 32:
        return 126-(32-asciiIndex)
    else:
        return asciiIndex