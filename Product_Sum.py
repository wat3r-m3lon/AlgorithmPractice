# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# Time complexity O(n) n is the total element in tha array,for instance [1,[1,2]] means n=4
# Spce complexity O(d) d is the max deepth
def productSum(array,deepth=1):
    # Write your code here.
    sum=0
    for element in array:
        if type(element) is list:
            sum+=productSum(element,deepth+1)
        else:
            sum+=element
    return sum*deepth
    
