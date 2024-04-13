# Implement an algorithm to find the kth to last element of a singly linked list.

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
    
    def kthToLast_1(self, k):
        # This method counts the number of nodes and then gives kth to last node
        n = 0
        curr_node = self.head
        while curr_node:
            n += 1
            curr_node = curr_node.next
        
        n = n - k
        curr_node = self.head
        for i in range(n):
            curr_node = curr_node.next
        print("Kth to the last element:")
        print(curr_node.data)
    
    def kthToLast_2(self, k):
        # this method uses a loop to check is k nodes after the current node exist
        curr_node = self.head
        while curr_node:
            temp = curr_node
            for i in range(int(k)):
                temp = temp.next
            if not temp:
                print("Kth to the last element:")
                print(curr_node.data)
                return
            curr_node = curr_node.next
        
    def kthToLast_3(self, k):
        # 2 poiner approach where both pointers are k steps apart at the start and then move simultaneously
        # When 2nd pointer reaches end the first pointer is at Kth to last element

        point1 = self.head
        point2 = self.head

        for i in range(k):
            point2 = point2.next
        
        while point2:
            point1 = point1.next
            point2 = point2.next
        print("Kth to the last element:")
        print(point1.data)



ll = LinkedList()
print("Enter list data:")
for i in range(5):
    ll.insertAtEnd(int(input()))

print("Enter K:")
ll.kthToLast_3(int(input()))
