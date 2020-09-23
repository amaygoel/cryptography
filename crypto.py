import math
import random
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted = ""
    for char in plaintext:
        if(ord(char) > (ord("Z") - offset)):
            characterValue = ord("A") - 1 + (offset - (ord("Z") - ord(char)))
            encrypted += chr(characterValue)
        else:
            encrypted += chr(ord(char)+offset)
        print(char)

    return encrypted

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decrypted = ""
    for char in ciphertext:
        if(ord(char) < (ord("A") + offset)):
            characterValue = ord("Z") + 1 - (65+offset - ord(char))
            decrypted += chr(characterValue)
        else:
            decrypted += chr(ord(char)-offset)
        print(char)

    return decrypted

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypted = ""
    j = 0
    length = len(plaintext)
    times = math.floor(len(plaintext) / len(keyword))
    remainder = len(plaintext) % len(keyword)
    expandedKey = ""
    for i in range (0, times):
        expandedKey += keyword
    if(remainder > 0):
        for i in range (0,remainder):
            expandedKey += keyword[i]
    print(expandedKey)
    for char in plaintext:
        newValue = ord(char) + (ord(expandedKey[j])-65)
        if newValue > 90:
            newValue = 64 + (newValue - 90)
        encrypted += chr(newValue)
        j += 1

    return encrypted

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypted = ""
    j = 0
    length = len(ciphertext)
    times = math.floor(len(ciphertext) / len(keyword))
    remainder = len(ciphertext) % len(keyword)
    expandedKey = ""
    for i in range (0, times):
        expandedKey += keyword
    if(remainder > 0):
        for i in range (0,remainder):
            expandedKey += keyword[i]
    print(expandedKey)
    for char in ciphertext:
        newValue = ord(char) - (ord(expandedKey[j])-65)
        if newValue < 65:
            newValue = 91 - (65 - newValue)
        decrypted += chr(newValue)
        j += 1

    return decrypted

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    total = 1
    W = []
    for i in range(0,n):
        num = random.randint(total+1,2*total)
        W.append(num)
        total += num
    Q = random.randint(total+1,2*total)
    R = 0
    for j in range(2, Q-1):
        if(math.gcd(j,Q)==1):
            R = j
            break
    return [W,Q,R]




# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    B = []
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    for i in range(0,len(W)):
        num = R * W[i] % Q
        B.append(num)
    return B

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    # print(encrypt_caesar("AXYZ", 3))
    # print(decrypt_caesar("DABC", 3))
    print(encrypt_vigenere("ATTACKATDAWN","LEMON"))
    print(decrypt_vigenere("EAAAEEEE","BBB"))
    print(generate_private_key())
    print(create_public_key(generate_private_key()))

if __name__ == "__main__":
    main()