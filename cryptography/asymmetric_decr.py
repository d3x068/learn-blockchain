from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# load the private key
with open('private_key.pem','rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend = default_backend()
    )

# load the ciphertext
with open('asym.encrypted','rb') as f:
    ciphertext = f.read()

# decrypt using private key
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

print(plaintext.decode('utf-8'))

# write the plaintext
with open('asym.decrypted','w') as f:
    f.write(plaintext.decode('utf-8'))