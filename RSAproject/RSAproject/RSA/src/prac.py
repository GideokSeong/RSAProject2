from crypto.Cipher import aes
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import rsa


def main():
    
    aeskey = Random.new().read(32)
    iv = Random.new().read(aes.block_size)
    cipher = aes.new(aeskey, aes.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')

    message = aeskey
    random_generator = Random.new().read
    rsakey = RSA.generate(1024, random_generator)
    cipher = PKCS1_OAEP.new(rsakey.publickey())
    ciphertext = cipher.encrypt(message)

    """Message = "Hi How are you"
    pubk, privk = rsa.newkeys(1024, poolsize=8)

    aes_key = rsa.randnum.read_random_bits(512)


    #print(aes_key)

    encrypted_aes_key = rsa.encrypt(aes_key, pubk)
    print(encrypted_aes_key)
    #f = rsa.encrypt(Message, encrypted_aes_key.decode())
    #print(f)
    #encypted = rsa.encrypt(Message, encrypted_aes_key)
    #print(encypted)

    t = rsa.decrypt(encrypted_aes_key, privk)
    print(t)




    #print(encrypted_aes_key)
    #print(t)"""

if __name__ == '__main__':
    main()