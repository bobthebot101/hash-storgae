import base64
import pyAesCrypt
import os


file = open('encrypted.txt', 'rb')
byte = file.read()

fh = open('data.txt', 'wb')
fh.write(base64.b64decode((byte)))
fh.close()


bufferSize = 64 * 1024
password = "BobjaneTmart1234567890"

pyAesCrypt.decryptFile("data.txt", "pic.png", password, bufferSize)
os.remove('encrypted.txt')
os.remove('data.txt')
