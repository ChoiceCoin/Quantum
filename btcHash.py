import hashlib
import secrets
import binascii
from binascii import unhexlify, hexlify
################################
print("##########################################################")
################################
# Version + hashPrevBlock + hashMerkleRoot + Time + Bits + Nonce
# print("##########################################################")
################################

# Variables

Version = "01000000"
hashPrevBlock = "0000000000000000000571509eac4819dae8ff2c320c487cfd612d36db7ffe1a"
hashMerkleRoot = "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b"
Time = "1672956895"
Bits = "1708417e"
Nonce = "42014695"

# Functional Hash
header_hex = (Version + hashPrevBlock + hashMerkleRoot + Time + Bits + Nonce)
header_bin = unhexlify(header_hex)
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
hexyh = hexlify(hash).decode("utf-8")
newBlockHash = hexlify(hash[::-1]).decode("utf-8")
print("preBlockHash", hashPrevBlock)
print("newBlockHash", newBlockHash)
