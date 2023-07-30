import hashlib
import secrets
import binascii
from binascii import unhexlify, hexlify
import csv
import random

################################
print("##########################################################")
################################
# Version + hashPrevBlock + hashMerkleRoot + Time + Bits + Nonce
# print("##########################################################")
#pen(list2.csv,'r') as version

################################
with open('list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for i in row:
            def ensure_10_digits(i):
                if len(i) >= 10:
                    i = i
                    print(i)
                else:
                    additional_digits = ''.join(str(random.randint(0, 9)) for _ in range(10 - len(i)))
                    i = i + additional_digits
                    print(i)
            Nonce = str(i)
            with open('list2.csv', 'r') as file2:
                reader2 = csv.reader(file2)
                for row2 in reader2:
                    for i2 in row2:
                        def ensure_8_digits(i2):
                            if len(i2) >= 8:
                                i2 = i2
                                print(i2)
                            else:
                                additional_digits = ''.join(str(random.randint(0, 9)) for _ in range(8 - len(i2)))
                                i2 = i2 + additional_digits
                                print(i2)
                        ensure_8_digits(i2)
                        # Variables
                        Version = str(i2)
                        Nonce = str(i)
                        Version = str(i2)
                        hashPrevBlock = "0000000000000000000571509eac4819dae8ff2c320c487cfd612d36db7ffe1a"
                        hashMerkleRoot = "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b"
                        Time = "1672956895"
                        Bits = "1708417e"
                            # Variables
                            #Version = "01000000"
                            #hashPrevBlock = "0000000000000000000571509eac4819dae8ff2c320c487cfd612d36db7ffe1a"
                            #hashMerkleRoot = "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b"
                            #Time = "1672956895"
                            #Bits = "1708417e"
                            #Nonce = "42014695"
                            # Check
                            #nonce_guess(Nonce)
                        header_hex = (Version + hashPrevBlock + hashMerkleRoot + Time + Bits + Nonce)
                        def process_header(header_hex):
                            if len(header_hex) % 2 == 0:
                                header_bin = unhexlify(header_hex)
                                hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
                                hexyh = hexlify(hash).decode("utf-8")
                                newBlockHash = hexlify(hash[::-1]).decode("utf-8")
                                print("preBlockHash", hashPrevBlock)
                                print("newBlockHash", newBlockHash)

                                def count_leading_zeros(hash_value):
                                    count = 0
                                    for i, char in enumerate(hash_value):
                                        if char == "0":
                                            count += 1
                                        else:
                                            break
                                    return count
                                count_prev = count_leading_zeros(hashPrevBlock)
                                count_new = count_leading_zeros(newBlockHash)
                                if count_new >= count_prev:
                                    print("found")
                                    return

                            else:
                                # add a leading zero to make the string an even length
                                header_hex = "0" + header_hex
                                header_bin = unhexlify(header_hex)
                                hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
                                hexyh = hexlify(hash).decode("utf-8")
                                newBlockHash = hexlify(hash[::-1]).decode("utf-8")
                                print("preBlockHash", hashPrevBlock)
                                print("newBlockHash", newBlockHash)
                                def count_leading_zeros(hash_value):
                                    count = 0
                                    for i, char in enumerate(hash_value):
                                        if char == "0":
                                            count += 1
                                        else:
                                            break
                                    return count
                                count_prev = count_leading_zeros(hashPrevBlock)
                                count_new = count_leading_zeros(newBlockHash)
                                if count_new >= count_prev:
                                    print("found")
                                    return

                        process_header(header_hex)
