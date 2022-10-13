import hashlib, itertools

def brute_force(hash):
    elements = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    i = 0
    for element in itertools.product(elements, repeat=4):
        nonce_try = ''.join(element)
        i = i + 1
        key = hashlib.sha256(nonce_try.encode()).hexdigest()
        print(key)
        if hashlib.sha256(nonce_try.encode()).hexdigest() == hash:
            print('count = ',i)
            return nonce_try
    
            

#target_hash = "002b6e7c5ae57940f53862b0f09ae969c86c305d93e10c39e2dcf583a3dd1608"
target_hash = "002b"
key = hashlib.sha256(target_hash.encode()).hexdigest()
print("Hash: %s" % key)
print("Calling quantum oracle.")
recovered_key = brute_force(key)
print("Brute-force result: %s" % recovered_key) 
