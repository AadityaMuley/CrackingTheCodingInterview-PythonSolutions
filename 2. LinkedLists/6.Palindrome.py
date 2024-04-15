# Implement a function to check if a linked list is a palindrome.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
    
def checkPalindrome(ll):
    slow = ll.head
    fast = ll.head
    half1 = []

    while fast and fast.next:
        half1.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    
    half2 = []
    while slow:
        half2.insert(0, slow.data)
        slow = slow.next
    
    if len(half1) != len(half2):
        half2.pop()
    
    if half1 == half2:
        return True
    else:
        return False

print("Enter list elements:")
ll = LinkedList()
for i in range(5):
    ll.insertAtEnd(input())

print(" ")

check  = checkPalindrome(ll)
if check:
    print("Palindrome")
else:
    print("Not Palindrome")