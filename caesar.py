import string

def alphabet_position(letter):

    alphabet = string.ascii_lowercase

    return alphabet.find(letter.lower())

def rotate_character(char, rot):

    alphabet = string.ascii_lowercase

    a_char = char
    if a_char in string.ascii_letters:
        pos = alphabet_position(char)
        rotated_pos = (pos + rot) % 26

        if char in string.ascii_lowercase:
            a_char = alphabet[rotated_pos]
        else:
            a_char = alphabet[rotated_pos].upper()

    return a_char

def rotate_string(text, rot):
    encrypted_string = ''

    for chr in text:
        encrypted_string += rotate_character(chr, rot)

    return encrypted_string
