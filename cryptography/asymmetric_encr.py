from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding,rsa

plaintext = b'This message is secret'

# load the private key
# with open('private_key.pem','rb') as f:
#     private_key = serialization.load_pem_private_key(
#         f.read(),
#         password = None,
#         backend = default_backend()
#     )

# load the public key
with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend = default_backend()
    )

# encrypt the message using the public key
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

print(ciphertext)

with open('asym.encrypted','wb') as f:
    f.write(ciphertext)