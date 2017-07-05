from __future__ import absolute_import, division, print_function, unicode_literals

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_arc4(key, plaintext):
    cipher = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext)


def decrypt_arc4(key, ciphertext):
    cipher = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext)


def decrypt_aes(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), mode=modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext)


def digest_md5(*values):
    d = hashes.Hash(hashes.MD5(), backend=default_backend())
    for value in values:
        d.update(value)
    return d.finalize()


def digest_sha256(*values):
    d = hashes.Hash(hashes.SHA256(), backend=default_backend())
    for value in values:
        d.update(value)
    return d.finalize()
