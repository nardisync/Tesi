
# CRITTOGRAFIAMO UN FILE E LO DECRIPTIAMO
from cryptography.fernet import Fernet

# Prendiamo la key dal file
file = open('key.key', 'rb')
key = file.read()
file.close()

# Apriamo il file da encriptare
with open('psw.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# Scriviamo il file encriptato
with open('test.txt.encrypted', 'wb') as f:
    f.write(encrypted)
    # l'originale è ancora presente però
    # dovremmo cancellarlo


# Leggiamo i dati dal file criptato
with open('test.txt.encrypted', 'rb') as f:
    data = f.read()
fernet = Fernet(key)
decrypted = fernet.decrypt(data)

# Scriviamo il file decriptato
with open('test.txt.decrypted', 'wb') as f:
    f.write(decrypted)
    # l'originale è ancora presente però
    # dovremmo cancellarlo


'''
# LETTURA DI UNA CHIAVE DA UN FILE E CODIFICA MESSAGGI 
from cryptography.fernet import Fernet

# Prendiamo la key dal file
file = open('key.key', 'rb')
key = file.read()
file.close()

# Encode del messaggio
messaggio = "my deep dark secret"
encode = messaggio.encode()

# Criptiamo il messaggio
f = Fernet(key)
encrypted = f.encrypt(encode)
print(encrypted)

#Riprendiamo la Key per pura dimostrazione
file = open('key.key', 'rb')
key2 = file.read()
file.close()

# Decriptiamo il messaggio
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
print(decrypted)

# Decodifichiamo il mesaggio
original_message = decrypted.decode()
print(original_message)
'''






'''
# Crea sempre la stessa key ad ogni avvio
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provide = "password" # Input nella forma di stringa
password = password_provide.encode() #Convert to type bytes

# print(os.urandom(16))
salt = b'\xe3\x8d\xa4\x18Y\n\x1c\xe6\x9bd\xf9\xb4\xf3`\x98\xe0'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=10000,
    backend=default_backend()
)
key = base64.urlsafe_b64decode(kdf.derive(password)) # Può usare kdf solo una volta
print(key)
'''


'''

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

# Scriviamo la Key su un file
file = open('key.key', 'wb')
file.write(key)
file.close()

# Apèriamo il file e leggiamo la key
file = open('key.key', 'rb')
key1 = file.read()
file.close()
print(key1)

'''