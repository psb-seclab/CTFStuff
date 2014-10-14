"""
Modify this script to suit your needs
"""

import os, random, struct
from Crypto.Cipher import AES

def encrypt_bmp(key, iv, mode, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        iv:
            encryption iv

        mode:
            encryption mode

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    #iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    if mode == AES.MODE_ECB:
        # no iv is needed for ECB!
        encryptor = AES.new(key, AES.MODE_ECB)
    elif mode == AES.MODE_CBC:
        encryptor = AES.new(key, AES.MODE_CBC, iv)
    else:
        print "invalid mode, program stopped"
        return

    with open(in_filename, 'rb') as infile:
        # extract bmp header
        header = infile.read(54)
        # open output file
        with open(out_filename, 'wb') as outfile:
            outfile.write(header)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def main():
    # test to encrypt & decrypt a file
    in_file = 'pic_original.bmp'
    mode_ecb = AES.MODE_ECB
    mode_cbc = AES.MODE_CBC
    key = 16*'a'
    iv = 16*'\x00'
    
    encrypt_bmp(key, iv, mode_ecb, in_file, 'pic_original_ecb.bmp', 1024)
    encrypt_bmp(key, iv, mode_cbc, in_file, 'pic_original_cbc.bmp', 1024)

    #encrypt_file(key, in_file, None, 1024)
    #decrypt_file(key, in_file+'.enc', in_file+'.out', 1024)


if __name__ == "__main__":
    main()
