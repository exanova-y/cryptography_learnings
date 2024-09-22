# rsa implementation
# note
import random
import math


# key generation
# check if it's prime

def is_prime(n):
    if n < 2: # is one.
        return False
    elif n%2==0: # even numbers are not prime.
        return False 
    # make sure this is int, not float
    for i in range(3, int((n)**0.5)+1, 2):
        if n%i==0:
            return False
    return True


def generate_prime(min_val, max_val):
    n = random.randint(min_val, max_val)
    while not is_prime(n):
        n = random.randint(min_val, max_val)
    return n
        

def mod_inv(public, phi_n_value):
    # need to find modular inverse

    # d*e = (k*phi_n)+1
    # d = (k*phi_n + 1)/e
    # you should use the extended euclidean algorithm, which finds the GCD of two numbers in this case, to be faster
    for private in range(3, phi_n_value):
        if (private*public)%phi_n_value==1:
            print("found a mod inverse.")
            return private
        
    raise ValueError("mod inv does not exist.")
    # get the first value 
    # the first k (scalar before phi_n) makes the term divisible by e will be used

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

def generate_keys():
    print('prime number generation begins.')
    p = generate_prime(10**8, 10**9)
    q = generate_prime(10**8, 10**9) # small primes for poc. should be 
    while p == q:
        q = generate_prime(1000, 5000)
    print("begin computing n")
    n = p*q
    bin_n = bin(n)[2:]
    print("number bits of n:", len(bin_n))

    # there is no efficient factorization algorithm.
    phi_n = (p-1)*(q-1) # euler's totient function
    print("begin generating public and private keys")
    e = random.randint(3, phi_n-1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n-1)
        # generate private key
    d = mod_inv(e, phi_n) 
    return p, q, n, phi_n, e, d
    print("key generation complete.")


def report():
    print("For the reader:")
    print ("Prime number p: ", p_val)
    print ("Prime number q: ", q_val)
    print ("Public Key: ", e_val)
    print ("Private Key: ", d_val)
    print ("n: ", n_val)
    print ("phi(n): ", phi_n_val)


# encryption
def encrypt(x_plaintext, e, n):
    print("ascii-fying")
    # get ascii representation of a message
    x_ascii = [ord(c) for c in x_plaintext]
    # will look like: 100, 98, 100, etc etc in a list
    cipher = [pow(ch, e, n) for ch in x_ascii] 
    return cipher


# decryption
def decrypt(y, d, n):
    y_ascii = [pow(ch, d, n) for ch in y]
    y_decoded = "".join([chr(ch) for ch in y_ascii]) # would return a list of individual letters
    # pass it into join function, so items can be connected
    return y_decoded


def crack():
    # try to get private key d
    pass

# actual process:
p_val, q_val, n_val, phi_n_val, e_val, d_val = generate_keys()
report()
# hardcode for now, make it input for later
message = "english is mind control"
ciphertext = encrypt(message, e_val, n_val)
print("encoded message:", ciphertext)
decrypt(ciphertext, d_val, n_val)