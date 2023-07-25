import numpy as np

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix))) # Calculate determinant and round to an integer
    det_inv = None

    for i in range(1, modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break

    if det_inv is None:
        raise ValueError("Matrix is not invertible.")

    # Calculate the inverse matrix
    matrix_mod_inv = np.round(det_inv * np.linalg.inv(matrix) * det) % modulus

    return matrix_mod_inv.astype(int)

def text_to_matrix(text, n):
    matrix = []

    for char in text:
        matrix.append(ord(char) - ord('A'))

    while len(matrix) % n != 0:
        matrix.append(23) # Pad with 'X' (corresponds to 23 in Hill cipher)

    return np.array(matrix).reshape(-1, n)

def matrix_to_text(matrix):
    text = ""

    for num in matrix.flatten():
        text += chr(num + ord('A'))

    return text

def encrypt(plain_text, key):
    n = len(key)
    matrix = text_to_matrix(plain_text, n)

    # Convert the key to a matrix
    key_matrix = np.array(key)

    encrypted_matrix = np.dot(matrix, key_matrix) % 26
    encrypted_text = matrix_to_text(encrypted_matrix)

    return encrypted_text

def decrypt(cipher_text, key):
    n = len(key)
    matrix = text_to_matrix(cipher_text, n)

    key_matrix = np.array(key)

    # INVERSE OF MATRIX FOR DECRYPTION
    key_matrix_inv = matrix_mod_inv(key_matrix, 26)

    decrypted_matrix = np.dot(matrix, key_matrix_inv) % 26
    decrypted_text = matrix_to_text(decrypted_matrix)

    return decrypted_text

# OUTPUT 
key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
plaintext = "ADITYASHA"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)
