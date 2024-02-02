'''semordnilap'''
# O(n*m) for both space and time complexity
def semordnilap(words):
    # Write your code here.
    wordsl=set(words)
    semordnilaps=[]
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in wordsl and reversed_word != word:
            semordnilaps.append((word, reversed_word))
            wordsl.remove(word)
            wordsl.remove(reversed_word)

    return semordnilaps
    
    
