"""

Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".

Sample input:"xyz", 2 Sample output:"zab"


"""

"""
o(n),o(n)
"""

def caesarCipherEncryptor(string, key):
    # Write your code here.
    new_string=""

    for char in string:
        charIndex=ord(char)-ord('a')
        shift=(charIndex+key)%26
        newChar=chr(shift+ord('a'))
        new_string+=newChar
    return new_string
    

