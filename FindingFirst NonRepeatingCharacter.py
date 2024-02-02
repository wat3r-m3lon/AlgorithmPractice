def firstNonRepeatingCharacter(string):
    # Write your code here.
    count={}
    for char in string:
        if char not in count:
            count[char]=0
        count[char]+=1
    for i in range(len(string)):
        char =string[i]
        if count[char]==1:
            return i
    return -1