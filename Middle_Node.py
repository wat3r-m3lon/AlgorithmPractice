"""

"""

# Define the LinkedList class as before
#time O(n), space  O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Function to find the middle node using two pointers
def middleNode(linkedList):
    slow = fast = linkedList
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


#time O(n) space O(1)
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    counter=0
    cur=linkedList
    while cur is not None:
        counter+=1
        cur=cur.next
    mid = linkedList
    for _ in range(counter//2):
        mid=mid.next
    return mid
    
