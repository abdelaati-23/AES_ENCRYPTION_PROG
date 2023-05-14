#!/usr/bin/env python3
from Crypto.Cipher import AES
import os
class Encryption:
    def __init__(self, key):
        self.key = key

    def encrypt_message(self, message):
        BLOCK_SIZE = 16
       # IV = bytes([0] * BLOCK_SIZE)
        IV = os.urandom(BLOCK_SIZE)

        cipher = AES.new(self.key, AES.MODE_CBC, IV)

        padding_length = BLOCK_SIZE - (len(message) % BLOCK_SIZE)
        message += bytes([padding_length]) * padding_length

        encrypted_data = IV + cipher.encrypt(message)

        return encrypted_data

    def decrypt_message(self, encrypted_data):
        BLOCK_SIZE = 16
        IV = encrypted_data[:BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_CBC, IV)

        decrypted_data = cipher.decrypt(encrypted_data[BLOCK_SIZE:])

        padding_length = decrypted_data[-1]
        decrypted_data = decrypted_data[:-padding_length]

        return decrypted_data

    def encrypt_file(self, input_file_path, output_file_path):
        BLOCK_SIZE = 16
       # IV = bytes([0] * BLOCK_SIZE)
        IV = os.urandom(BLOCK_SIZE)
        cipher = AES.new(self.key, AES.MODE_CBC, IV)

        with open(input_file_path, 'rb') as infile:
            data = infile.read()

        padding_length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
        data += bytes([padding_length]) * padding_length

        encrypted_data = IV + cipher.encrypt(data)

        with open(output_file_path, 'wb') as outfile:
            outfile.write(encrypted_data)

    def decrypt_file(self, input_file_path, output_file_path):
        BLOCK_SIZE = 16
        with open(input_file_path, 'rb') as infile:
            encrypted_data = infile.read()

        IV = encrypted_data[:BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_CBC, IV)

        decrypted_data = cipher.decrypt(encrypted_data[BLOCK_SIZE:])

        padding_length = decrypted_data[-1]
        decrypted_data = decrypted_data[:-padding_length]

        with open(output_file_path, 'wb') as outfile:
            outfile.write(decrypted_data)

while True:
    key = input("Enter the key to use for encryption and decryption (must be 16 bytes): ").encode('utf-8')
    if len(key) == 16:
        break
    else:
        print("Invalid key length. Please enter a key that is 16 bytes long.")

encryption = Encryption(key)

choice = input("Do you want to encrypt a file (F) or a message (M)? ")
if choice.upper() == "F":
    encryption_or_decryption = input("Do you want to encrypt (E) or decrypt (D)? ")

    if encryption_or_decryption.upper() == "E":
        input_file_path = input("Enter the path of the input file: ")
        output_file_path = input("Enter the path of the output file: ")
        encryption.encrypt_file(input_file_path, output_file_path)
        print("File encrypted successfully!")
    elif encryption_or_decryption.upper() == "D":
        input_file_path = input("Enter the path of the input file: ")
        output_file_path = input("Enter the path of the decrypted output file: ")
        encryption.decrypt_file(input_file_path, output_file_path)
        print("File decrypted successfully!")
    else:
        print("Invalid choice!")
elif choice.upper() == "M":
     
        
         message = input("Enter the message to encrypt: ").encode('utf-8')
         encrypted_data = encryption.encrypt_message(message)
         print("Encrypted message:", encrypted_data)
         decrypted_data = encryption.decrypt_message(encrypted_data)
         print("Decrypted message:", decrypted_data.decode('utf-8'))
         
else:
    print("Invalid choice!")
