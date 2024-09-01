def binarySearch(array, target):
    # Time complexity O(logn), space compelxityO(1)
    
    left=0
    right =  len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = array[mid]

        if mid_value == target:
            return mid  # Target found, return index
        elif mid_value < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found

    
def binarySearch(array, target):
    # Time compleixty O(logn), space compleixty O(1)
    return helper(array,target,0, len(array)-1)

def helper(array, target,left,right):
    if left>right:
        return -1
    mid=(right+left)//2
    pot=array[mid]
    if target ==pot:
        return mid
    elif target< pot:
        return helper(array,target, left, mid-1)
    else:
        return helper(array, target, mid+1,right)
    
