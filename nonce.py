# The nonce in a bitcoin block is a 32-bit (4-byte) field whose value is adjusted by miners so that the hash of the block will be less than or equal to the current target of the network. 
# Target is a 256-bit number
# The lower the target, the more difficult it is to generate a block.
## difficulty = difficulty_1_target / current_target

# Map
# Run two algorithms in parallel to use a total of 1,792 qubits
# chimerra = 16 * 56
# num_variables = 896
# num_couplers = 1,176 couplers

import hashlib, itertools
import dimod
import random

# How do you assign an int value to SHA-256 hash.
# Break the assignment into smaller parts to filter possibilities.

# For target_hash:
    # nonce = hashlib(try_nonce)
    # if nonce < target_hash:
        # print(nonce)

# Nonce = range(0, 4,294,967,296)
def brute_force(hash):
    elements = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    i = 0
    for element in itertools.product(elements, repeat=10):
        nonce_try = ''.join(element)
        i = i + 1
        nonce = hashlib.sha256(nonce_try.encode()).hexdigest()
        print(nonce)
        if hashlib.sha256(nonce_try.encode()).hexdigest() == hash:
            #print('count = ',i)
            return nonce_try

#target_hash = "002b6e7c5ae57940f53862b0f09ae969c86c305d93e10c39e2dcf583a3dd1608"
target_hash = "002b6e7"
nonce = hashlib.sha256(target_hash.encode()).hexdigest()
print("Calling quantum oracle.")
recovered_nonce = brute_force(nonce)
print(nonce)


# Produce a number that when hashed is less than or equal to the target_hash.
x, y = dimod.Binaries(["x", "y"])
bqm = 2*x*y - x - y
#print(bqm.to_polystring())
-x - y + 2*x*y
#print(dimod.ExactSolver().sample(bqm).lowest())
#x = random(x)
#y = random(y)
#print(x)
#print(y)

x = dimod.Binary('x')
bqm = 3*x - 1.5
#print(bqm.to_polystring())
#print(x)

