# generate key using Fernet from cryptography library
from cryptography.fernet import Fernet

# generate shared key in binary format and it is base64 encoded
shared_key = Fernet.generate_key()
print(shared_key)

# create instance from that shared_key
fernet = Fernet(shared_key)

# encrypt
ciphertext = fernet.encrypt(b'Secret Message!')
print(ciphertext)

# write the ciphertext to a file
with open('message.encrypted','wb') as f:
    f.write(ciphertext)
    
# write the shared key to a file
with open('shared_key','wb') as f:
    f.write(shared_key)