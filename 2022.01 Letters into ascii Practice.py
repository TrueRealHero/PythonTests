# December 14 of 2022 ----------------------------------------

# import string

# def func():
#     sentence = "The sunset sets at twelve o' clock."
#     x = list()
#     for i in sentence:
#         if i == string.ascii_letters.index(sentence):
#             x.append(i)
#     return x
    
# word_to_ascii = func()
# print(word_to_ascii)

from string import ascii_lowercase

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers)

sentence = "The sunset sets at twelve o' clock."
x = alphabet_position(sentence)
print(x)

# Best Solution
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())