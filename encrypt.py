import pyAesCrypt
import os
import base64 
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "BobjaneTmart1234567890"
# encrypt
pyAesCrypt.encryptFile("ClipDrop.dmg", "data.txt", password, bufferSize)
os.remove('ClipDrop.dmg')

with open('data.txt', 'rb') as imagefile:
  byteform = base64.b64encode(imagefile.read())


f = open('encrypted.txt', 'wb')
f.write(byteform)
f.close()
os.remove('data.txt')
