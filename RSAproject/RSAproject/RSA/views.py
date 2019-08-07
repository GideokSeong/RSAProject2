from django.shortcuts import render
from django.views.generic import TemplateView
from .src import rsaSipher, RSAHome
from django.urls import reverse
import rsa
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


class HomePageView(TemplateView):

    def get(self, request, **kwargs):

        return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'about.html')


def SpecifyFileNamesPageView(request):

    # File names for creating a public key and a private key

    if request.method == 'POST':
        filename = request.POST.get('text1')
        RSAHome.main(filename)

    return render(request, 'SpecifyFileName.html')


def upload_file_encrypt(request):

    if request.method == 'POST' and request.FILES['myfile'] and request.FILES['pubkeyfile']:
        myfile = request.FILES['myfile']
        pubkey = request.FILES['pubkeyfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        # Store the data from the file to be used for encryption

        publickey = b""
        for i in pubkey:

            #i = i.decode(encoding="ISO-8859-1", errors='ignore')

            publickey = publickey + i
        #publickey = publickey.encode()

        message = b""

        for i in myfile:
            #print(type(i))
            #i = i.encode('utf8')
            #i = i.decode(encoding="ISO-8859-1", errors='ignore')

            message = message + i

        #message = str.encode(message)
        # Push the message and get the encrypted message and the decrypted message
        filename, enc = RSAHome.encryptData(message, publickey)

        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'filename': filename,
            'encrypted': enc
        })

    return render(request, 'simple_upload.html')


def upload_file_to_decrypt(request):

    if request.method == 'POST' and request.FILES['myfile2'] and request.FILES['privkeyfile']:
        myfile2 = request.FILES['myfile2']
        private = request.FILES['privkeyfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile2.name, myfile2)
        uploaded_file_url = fs.url(filename)

        fe = open("encrypted_file.txt", 'rb')
        crypto = fe.read()
        #print("crypto1:", crypto)

        encrypted = b""

        for i in myfile2:
            #i = i.decode(encoding="utf-16", errors='ignore')
            encrypted = encrypted + i

        #print("crpyto2 decryp:", encrypted)
        #encrypted = encrypted.encode()
        #print("crypto2:", encrypted)

        privatekey = b""
        for i in private:

            #i = i.decode(encoding="ISO-8859-1", errors='ignore')
            privatekey = privatekey + i
        #privatekey = privatekey.encode()
        #print(privatekey)
        # Push the message and get the encrypted message and the decrypted message
        filename, dec = RSAHome.decryptData(encrypted, privatekey)

        return render(request, 'upload_file_to_decrypt.html', {
            'uploaded_file_url': uploaded_file_url,
            'filename': filename,
            'decrypted': dec
        })

    return render(request, 'upload_file_to_decrypt.html')





