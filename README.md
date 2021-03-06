# Easy Encryption

Source: [https://github.com/WKHAllen/easyencrypt](https://github.com/WKHAllen/easyencrypt)

### Contents

Hashing, symmetric encryption, and public/private key encryption functions.

### Dependencies

* [cryptography](https://github.com/pyca/cryptography)
* [rsa](https://github.com/sybrenstuvel/python-rsa/)

### Installation

`pip install easyencrypt`

### Example

```python
>>> # hashing
>>> from easyencrypt import newSalt, hashText
>>> newSalt()
b"b\xa3\x1c\xf5Y\xe2;\xb9\xa6\xaeUz\xde\x88\x07\xfe'\xc9\xaa\x96\xdfBh\xc9\xf9\x04\xb26\xff\xa9zJ\x17\xd5\x01n\xfeV\xa7$\xa8`G\xfd\r]\x8a`\xeaL4\x02{\xd6\x9b\xb3\xa9\xd9\x89\x18;\xec\xab\x83"
>>> message = "Hello, World!"
>>> hashText(message, algorithm="sha256")
b'\xdf\xfd`!\xbb+\xd5\xb0\xafgb\x90\x80\x9e\xc3\xa51\x91\xdd\x81\xc7\xf7\nK(h\x8a6!\x82\x98o'
>>> # symmetric encryption/decryption
>>> from easyencrypt import newKey, passwordToKey, symmetricEncrypt, symmetricDecrypt
>>> newKey()
b'1h8_Z3LcL55r3ljklF_1fhKWy122zqDYWAJyQEZaKlA='
>>> password = "password123"
>>> key = passwordToKey(password)
>>> key
b'75K3eLr-dx6JJFuJ7LwIpEpOFmwGZZkRiB84PURz6U8='
>>> ciphertext = symmetricEncrypt(message, key)
>>> ciphertext
b"\x80\x00\x00\x00\x00[B?\xe7\xbb\x825s\xff\xf3\x92AX|$\xf5\x19\x16\xe7f\x98\x8cgND\xf8\xdf\xd4Q\x00Y\xe5v\xb9\x0e\xa0\xa0\xb8\x05\x87N\xe6\x19h\x93K\xa9\xdb\x11\xef%V\xc2\xb1'\xa4;\xb8\xaf\xd2[\xdc\xb2\xae\xea\xca\xa4z"
>>> symmetricDecrypt(ciphertext, key)
b'Hello, World!'
>>> # public/private key encryption/decryption
>>> from easyencrypt import newKeyPair, encrypt, decrypt
>>> pub, priv = newKeyPair()
>>> ciphertext = encrypt(message, pub)
>>> ciphertext
b"\x01@H\x16\xe5\x01\xc0\x02)\x13\x8e\xba\xbb{p_5t\xf1\x81\x18y2\x12=t\xfe\xeb(\xcf\xce\xdd\xbd'\xb2\xddS\xbd\x0e\xc3\xf5\x0b-\xd8{\xe3W\xd5\xe8)_\xa8\xfb\x11\x8d\xb2\xb0l\x04\xf2>\xd9`\x0cS\xb9"
>>> decrypt(ciphertext, priv)
b'Hello, World!'
```
