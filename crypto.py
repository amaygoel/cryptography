# imports
import math
import random

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(plaintext) == 0:
        print("empty string")
    else:
        for char in plaintext:
            if char not in alphabet:
                encrypted += char
            elif(ord(char) > (ord("Z") - offset)):
                characterValue = ord("A") - 1 + (offset - (ord("Z") - ord(char)))
                encrypted += chr(characterValue)
            else:
                encrypted += chr(ord(char)+offset)

    return encrypted

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decrypted = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(ciphertext) == 0:
        print("empty string")
    else:
        for char in ciphertext:
            if char not in alphabet:
                decrypted += char
            elif(ord(char) < (ord("A") + offset)):
                characterValue = ord("Z") + 1 - (65+offset - ord(char))
                decrypted += chr(characterValue)
            else:
                decrypted += chr(ord(char)-offset)

    return decrypted

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypted = ""
    changingNum = 0
    expandedKey = ""
    if len(keyword) > len(plaintext):
        for num in range (0, len(plaintext)):
            expandedKey += keyword[num]
    else:
        times = math.floor(len(plaintext) / len(keyword))
        remainder = len(plaintext) % len(keyword)
        for num in range (0, times):
            expandedKey += keyword
        if(remainder > 0):
            for num in range (0,remainder):
                expandedKey += keyword[num]
    print(expandedKey)
    for char in plaintext:
        newValue = ord(char) + (ord(expandedKey[changingNum])-65)
        if newValue > 90:
            newValue = 64 + (newValue - 90)
        encrypted += chr(newValue)
        changingNum += 1

    return encrypted

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypted = ""
    changingNum = 0
    expandedKey = ""
    if len(keyword) > len(ciphertext):
        for num in range (0, len(ciphertext)):
            expandedKey += keyword[num]
    else:
        times = math.floor(len(ciphertext) / len(keyword))
        remainder = len(ciphertext) % len(keyword)
        for num in range (0, times):
            expandedKey += keyword
        if(remainder > 0):
            for num in range (0,remainder):
                expandedKey += keyword[num]
    print(expandedKey)
    for char in ciphertext:
        newValue = ord(char) - (ord(expandedKey[changingNum])-65)
        if newValue < 65:
            newValue = 91 - (65 - newValue)
        decrypted += chr(newValue)
        changingNum += 1

    return decrypted

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    total = 1
    W = []
    for num in range(0,n):
        value = random.randint(total+1,2*total)
        W.append(value)
        total += value
    Q = random.randint(total+1,2*total)
    R = 0
    for num in range(2, Q-1):
        if(math.gcd(num,Q)==1):
            R = num
            break
    return (tuple(W),Q,R)




# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    B = []
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    for element in W:
        num = (R * element) % Q
        B.append(num)
    return tuple(B)

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    C = []
    total = 0
    for char in plaintext:
        bits = byte_to_bits(ord(char))
        total = 0
        for num in range(0,8):
            value = int(bits[num])*int(public_key[num])
            total += value
        C.append(total)
    return C
        

# Arguments: an integer byte
# Returns: a list of integers
def byte_to_bits(byte):
    bits = []
    binary = bin(byte)[2:]
    for element in binary:
        bits.append(element)
    if len(bits) < 8:
        remainder = 8 % len(bits)
        for num in range(0, remainder):
            bits.insert(0,0)
    return bits


# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    S = findS(R, Q)
    decrypted = []
    for char in ciphertext:
        C = char * S % Q
        bitString = []
        for element in reversed(W):
            if element <= C:
                bitString.append(1)
                C -= element
            else:
                bitString.append(0)
        decrypted.append(chr(bits_to_byte(reversed(bitString))))
    
    return "".join(decrypted)

# Arguments: Q and R both integers
# Returns: an integer
def findS(R, Q):   
    for S in range(2,Q - 1):
        if (R * S % Q == 1):
            return S
    return 0

# Arguments: a list of integers
# Returns: an integer
def bits_to_byte(bits):
    bitsAsStrings = []
    byte = 0
    for element in bits:
        bitsAsStrings.append(str(element))
        bitString = "".join(bitsAsStrings)
        byte = int(bitString,2)
    return byte

# main - to test code
def main():
    # Testing code here
    p = generate_private_key()
    b = (create_public_key(p))
    print(b)
    print(p)
    x = (encrypt_mhkc("HELLO",b))
    print(x)
    print(decrypt_mhkc(x, p))

    private = ((10, 14, 35, 115, 248, 677, 1413, 3644), 10242, 5)
    public = (50, 70, 175, 575, 1240, 3385, 7065, 7978)
    message = "FOREACHEPSILONGREATERTHANDELTA"
    encrypted = encrypt_mhkc(message, public)
    print(encrypted)
    print(decrypt_mhkc(encrypted, private))

    print(encrypt_caesar("0DD !T$", 3))

if __name__ == "__main__":
    main()