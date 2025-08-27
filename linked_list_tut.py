# There are two types: Singly linked and doulby linked lists
# Single ones only point forwards, double points both ways

#Sinlgy Linked Lists:

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

#Traverse the list - O(n)

curr = Head

while curr:
    print (curr)
    curr = curr.next

#Display the linkedlist by throwing all elements in an array instead - O(n)

def display(Head):
    curr = Head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))

display(Head)

#Search for a node value O(n)

def search(Head, val):
    curr = Head
    while curr:
        if curr.val == val:
            return True
        else:
            curr = curr.next

    return False

print(search(Head, 2))
print(search(Head, 7))
print(search(Head, 1))