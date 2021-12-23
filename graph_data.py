import random


# initialize the graph as array and passing 2 parameteres
# 1. x,y position
# 2. adjascent nodes


graph = [
    # Node 0
    [(70, 210),  # x,y position
     (1, 2, 4, 6, 7)  # adjacent nodes
     ],
    # Node 1
    [(70, 350),  # Node 1
     (0, 2)
     ],
    [(140, 420),
        (0, 1, 5, 9, 10)
     ],
    [(210, 70),
        (11, 8, 6)
     ],
    [(210, 210),
        (0, 6, 7, 11, 12)
     ],
    [(210, 490),
        (2, 10)
     ],
    [(280, 140),
        (0, 3, 4, 11)
     ],
    [(280, 280),
        (0, 4, 9, 12)
     ],
    [(350, 70),
        (11, 3)
     ],
    [(350, 350),
        (2, 7, 10, 12, 13, 15)
     ],
    [(350, 490),
        (2, 5, 9, 13, 14, 15)
     ],
    [(420, 140),
        (3, 4, 6, 8, 12, 16, 17)
     ],
    [(420, 280),
        (4, 7, 9, 11, 17)
     ],
    [(420, 420),
        (9, 10, 15)
     ],
    [(490, 490),
        (10, 18, 15)
     ],
    [(560, 420),
        (9, 10, 13, 14, 17, 18)
     ],
    [(630, 70),
        (17, 11)
     ],
    [(630, 210),
        (11, 12, 15, 16, 18)
     ],
    [(700, 420),
        (17, 14, 15)
     ],


]

Battery = []


def randomBattery():
    for i in range(len(graph)):
        Battery.append(random.randrange(50, 100))






try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass
p=int(input('Enter prime p: '))
q=int(input('Enter prime q: '))
print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l
print("Choose an e from a below coprimes array:\n")
print(str(coprimes(phi)) + "\n")
e=int(input())
d=modinv(e,phi)
print("\nYour public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")
def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return c
def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")
enc = encrypt_string(s)
print("Encrypted message: " + enc + "\n")
dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")