from cryptography.fernet import Fernet

# open the ciphertext
with open('message.encrypted','rb') as f:
    ciphertext = f.read()

# open the shared key
with open('shared_key','rb') as f:
    shared_key = f.read()
    
fernet = Fernet(shared_key)
print(fernet.decrypt(ciphertext))