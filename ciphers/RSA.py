from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_key_pair():
    # Generate a new RSA key pair with a key length of 2048 bits
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Serialize the keys to bytes
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_bytes, public_key_bytes

private_key_bytes, public_key_bytes = generate_key_pair()

def RSA_encrypt(plaintext, public_key_bytes=public_key_bytes):
    # Deserialize the public key bytes to an RSA public key object
    public_key = serialization.load_pem_public_key(
        public_key_bytes,
    )

    # Encrypt the plaintext using RSA encryption with OAEP padding
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Return the ciphertext as bytes
    return ciphertext


def RSA_decrypt(ciphertext, private_key_bytes=private_key_bytes):
    # Deserialize the private key bytes to an RSA private key object
    private_key = serialization.load_pem_private_key(
        private_key_bytes,
        password=None,
    )

    # Decrypt the ciphertext using RSA decryption with OAEP padding
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Return the plaintext as a string
    return plaintext.decode()


