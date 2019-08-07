import rsa, sys, os
import rsa.randnum

# Generating publickey and privatekey using rsa module,
# poolsize allows to speed up


def main(filename):

    GenerateKey(filename, 2048)
    #name = file


def GenerateKey(name, keySize):

    publicKey, privateKey = rsa.newkeys(keySize, poolsize=8)

    aes_key = rsa.randnum.read_random_bits(512)
    encrypted_aes_key = rsa.encrypt(aes_key, publicKey)
    t = rsa.decrypt(encrypted_aes_key, privateKey)

    if os.path.exists('%s_pubkey.pem' % (name)) or os.path.exists('%s_privkey.pem' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! '
                 'Use a different name or delete these files and re-run this program.' % (name, name))

    print('The public key is %s of n and %s of e digit number.' % (len(str(publicKey['n'])), len(str(publicKey['e']))))
    print('The private key is %s of n and %s of e digit number.' % (len(str(privateKey['n'])), len(str(privateKey['e']))))

    print('Writing public key to file %s_pubkey.txt...' % (name))
    with open('%s_pubkey.pem' % (name), 'w') as outfile:
        outfile.write(publicKey.save_pkcs1().decode('ascii'))

    print('Writing private key to file %s_privkey.txt...' % (name))
    with open('%s_privkey.pem' % (name), 'w') as outfile:
        outfile.write(privateKey.save_pkcs1().decode('ascii'))


def encryptData(message, publickey):

    #fo = open('1_pubkey.pem', 'rb')
    #pubkey1 = fo.read()
    #fo.close()

    fo = open('1_privkey.pem', 'rb')
    privkey1 = fo.read()
    fo.close()

    with open('pubkey.pem', mode='rb') as publicfile:
        pubkey = publicfile.read()

    with open('privkey.pem', mode='rb') as privatefile:
        privkey = privatefile.read()

    pubkey = rsa.PublicKey.load_pkcs1(publickey)
    privkey = rsa.PrivateKey.load_pkcs1(privkey1)

    filename = 'encrypted_file.txt'
    crypto = rsa.encrypt(message, pubkey)

    #print(crypto)
    with open('encrypted_file.txt', 'wb') as outfile:
        outfile.write(crypto)

    #print(rsa.decrypt(crypto, privkey))

    return filename, crypto

def decryptData(crypto, privkey):

    #fo = open('1_privkey.pem', 'rb')
    #privkey = fo.read()
    #fo.close()
    #print(privkey)

    privkey = rsa.PrivateKey.load_pkcs1(privkey)
    filename = 'decrypted_file.txt'

    message = rsa.decrypt(crypto, privkey)
    fe = open(filename, 'wb+')
    fe.write(message)
    fe.close()

    return filename, message


if __name__ == '__main__':
    main()
