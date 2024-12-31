import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher

import secrets

# load public key
with open("public_key.pem",'rb') as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

# directory target
directory = './test'
output_directory = './test'
os.makedirs(output_directory,exist_ok=True)

# encrypt each file
for filename in os.listdir(directory):
    file_path = os.path.join(directory,filename)
    if os.path.exists(file_path):
        print(f'Encrypting {filename}..')
        
        # generate aes key and IV
        aes_key = secrets.token_bytes(32)
        iv = secrets.token_bytes(16)
        
        # encrypting process
        with open(file_path,'rb') as f:
            plaintext = f.read()
        
        cipher = Cipher()