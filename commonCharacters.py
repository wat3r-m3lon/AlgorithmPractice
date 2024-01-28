def commonCharacters(strings):
    characterCounts = {}
    
    # Loop over each string in the list of strings
    for string in strings:
        # Create a set of unique characters in the string
        uniqueStringCharacters = set(string)
        
        # Loop over each character in the set of unique characters
        for character in uniqueStringCharacters:
            # If the character is not already in the dictionary, initialize it to 0
            if character not in characterCounts:
                characterCounts[character] = 0
            # Increment the count for this character
            characterCounts[character] += 1
            
    # Initialize a list to store characters common to all strings
    finalCharacters = []
    
    # Loop over each character and its count in the dictionary
    for character, count in characterCounts.items():
        # If the count is equal to the number of strings, add to finalCharacters
        if count == len(strings):
            finalCharacters.append(character)
            
    # Return the list of common characters
    return finalCharacters
