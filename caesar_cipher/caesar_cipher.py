import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names


# ord()
# You can use the ord() method to convert a character to its numeric representation in Unicode

# chr()
# The chr() method accepts a number representing the Unicode of a character and returns the actual character corresponding to the numeric code

# Create an encrypt function that takes in a plain text phrase and a numeric shift
def encrypt(text, shift_key):
    encrypted_result = ""
    # traverse text
    for letter in text:
        if letter.isalpha():
            stay_in_alphabet = ord(letter) + shift_key 
        if stay_in_alphabet > ord('z'):
            stay_in_alphabet -= 26
        final_letter = chr(stay_in_alphabet)
        encrypted_result += final_letter
    print("Your ciphertext is: ", encrypted_result)
    return encrypted_result

# Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied
def decrypt(text, key):
    return encrypt(text, -key)

 
# check the above function
# turn these into tests
text = "attack"
s = 4
print("Cipher: " + encrypt(text, s))
print("Decipher: " + decrypt(encrypt(text, s), s))


# create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
word_list = words.words()
name_list = names.words()

def crack(text_to_crack):
    key = 1
    decrypt_guess = decrypt(text_to_crack, key)

    recognized_word_count = count_words(decrypt_guess)
    potential_word_count = len(text_to_crack.split())
    percentage = int(recognized_word_count / potential_word_count * 100)
    if percentage >= 50:
        return decrypt_guess

def count_words(text):
    candidate_words = text.split()
    word_count = 0
    for candidate in candidate_words:
        word = re.sub(r"[^A-Za-z]+", "", candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
    return word_count