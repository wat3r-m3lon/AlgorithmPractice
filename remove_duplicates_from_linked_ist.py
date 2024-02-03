'''
Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once. 
For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60. 
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    cur=linkedList
    while cur.next is not None:
        if cur.value==cur.next.value:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return linkedList


# This is an input class. Do not edit.
#This is the solution also working on the unsorted list
#The time complexity is O(n) pace complexity is O(n)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    current = linkedList
    prev = None
    seen = set()
    
    while current:
        if current.value in seen:
            prev.next = current.next  # Skip the current node
        else:
            seen.add(current.value)
            prev = current  # Only move prev if no duplicate was found
        current = current.next
    
    return linkedList


# This is an input class. Do not edit.
## using pointers. time: O(n^2) space O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next  # Remove duplicate
            else:
                runner = runner.next
        current = current.next
    
    return linkedList
