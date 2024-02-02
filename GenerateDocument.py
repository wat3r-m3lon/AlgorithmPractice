'''
You're given a string of available characters and a string representing a document that you need to generate. Write a function that determines if you can generate the document using the available characters. If you can generate the document, your function should return true; otherwise, it should return false.

You're only able to generate the document if the frequency of unique characters in the characters string is greater than or equal to the frequency of unique characters in the document string. For example, if you're given characters = "abcabc" and document = "aabbccc" you cannot generate the document because you're missing one c.

The document that you need to create may contain any characters, including special characters, capital letters, numbers, and spaces.

Note: you can always generate the empty string ("").
'''
# Time complexity: O(n+m) Space complexity; O(1)
def generateDocument(characters, document):
    # Count the occurrences of each character in 'characters'
    countc = {}
    for char in characters:
        if char not in countc:
            countc[char] = 0
        countc[char] += 1
        
    # Count the occurrences of each character in 'document'
    countd = {}
    for char in document:
        if char not in countd:
            countd[char] = 0
        countd[char] += 1

    # Check if 'characters' has enough of each character to create 'document'
    for char, count in countd.items():
        if char not in countc or countc[char] < count:
            return False
 
    return True

        
        