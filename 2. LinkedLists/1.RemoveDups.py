# Write code to remove duplicates from an unsorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def printList(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    def removeDuplicates(self):
        curr_node = self.head
        temp = self.head
        check = set()
        while curr_node:
            if curr_node.data not in check:
                check.add(curr_node.data)
                temp = curr_node
                curr_node = curr_node.next
            else:
                curr_node = temp
                curr_node.next = curr_node.next.next
                curr_node = curr_node.next

ll = LinkedList()
print("Enter Linked List:")
for i in range(5):
    ll.insertAtEnd(int(input()))

ll.removeDuplicates()

print("Final List:")
ll.printList()
