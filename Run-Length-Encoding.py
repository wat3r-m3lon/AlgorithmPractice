"""
Given a non-empty string, we are asked to write a function that is going to run-length-encode the input string and return the encoded string. 
Run-length encoding refers to replacing repetitive, consecutive data by a count and one copy of a repeated data. 
For instance, AAABB will be encoded as 3A2B. 
If a sequence contains more than 9 consecutive, identical characters, we first encode 9 characters, then the remaining ones. 
For instance, AAAAAAAAAA (10 As) will be encode as 9A1A.
"""

def runLengthEncoding(string):
    # Write your code here.
    output=""
    count=1
    current=string[0]
    for char in string[1:]:
        if char==current:
            count+=1
            if count==10:
                output+=f"9{current}"
                count=1
        else:
            output+=f"{count}{current}"
            current=char
            count=1
    output+=f"{count}{current}"
    return output

    