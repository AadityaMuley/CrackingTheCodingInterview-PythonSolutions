# Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, 
# given only access to that node.
# In this problem, you are not given access to the head of the linked list.
# EXAMPLE
# Input:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e- >f

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
    
    def printList(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    def getNode(self, value):
        # Find the first node with the given value.
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

def deleteNode(node):
    if node is None or node.next is None:
        return False  # Cannot delete the node
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    return True

ll = LinkedList()

print("Enter List:")
for i in range(5):
    ll.insertAtEnd(int(input()))


print("Enter the value of the node you want to delete (not the first or last):")
node_value = int(input())
node_to_delete = ll.getNode(node_value)

if node_to_delete is not None:
    if deleteNode(node_to_delete):
        print("Node deleted successfully.")
    else:
        print("Cannot delete the selected node (it might be the last node).")
else:
    print("Node not found.")

print("Final List:")
ll.printList()
