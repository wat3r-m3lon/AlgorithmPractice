'''
Palindrome Check
Write a function that takes in a non-empty string and that returns a boolean representing whether or not the string is a palindrome. A palindrome is dened as a string that is written the same forward and backward.

Sample input:"abcdcba"

Sample output: True (it is a palindrome)


'''

def isPalindrome(string):
    for i in range(len(string)//2):
        if string[i]!=string[len(string)-1-i]:
            return False
    return True