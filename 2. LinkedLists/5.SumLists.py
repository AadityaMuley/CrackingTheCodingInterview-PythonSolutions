# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1 's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295. 
# Output:2 -> 1 -> 9.Thatis,912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. 
# EXAMPLE
# Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. 
# Output:9 -> 1 -> 2.Thatis,912.

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

def sumFunc(num1, num2):
    # Function to calculate the sum of the 2 linked list numbers
    node1 = num1.head
    node2 = num2.head
    carry = 0
    ans = LinkedList()

    while node1 or node2:
        curr_sum = node1.data + node2.data + carry
        carry = int(curr_sum / 10)
        ans.insertAtBegin(int(curr_sum % 10))
        node1 = node1.next
        node2 = node2.next
    if carry != 0:
        ans.insertAtBegin(carry)
    
    return ans

num1 = LinkedList()
num2 = LinkedList()

print("Enter 1st num:")
for i in range(3):
    num1.insertAtEnd(int(input()))
print("Enter 2nd num:")
for i in range(3):
    num2.insertAtEnd(int(input()))

print("The Sum of the 2 nums is:")
ans = sumFunc(num1, num2)
ans.printList()
