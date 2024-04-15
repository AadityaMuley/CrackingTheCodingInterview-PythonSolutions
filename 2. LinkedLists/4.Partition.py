# Write code to partition a linked list around a value x, 
# such that all nodes less than x come before all nodes greater than or equal to x. 
# If x is contained within the list, the values of x only need to be after the elements less than x (see below). 
# The partition element x can appear anywhere in the "right partition"; 
# it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] 
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

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

    def insertAtBegin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

def partition(ll, part):
    # Function to partition the list elements
    curr_node = ll.head
    ans = LinkedList()
    while curr_node:
        if curr_node.data < part:
            ans.insertAtBegin(curr_node.data)
        else:
            ans.insertAtEnd(curr_node.data)
        curr_node = curr_node.next
    return ans

ll = LinkedList()

print("Enter original list:")
for i in range(5):
    ll.insertAtEnd(int(input()))
print("Enter partition element:")
part = int(input())

print("List after partition:")
ans = partition(ll, part)
ans.printList()