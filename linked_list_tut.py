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

#Doubly Linkedlists

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    
head = tail = DoublyNode(1)
print(head)
print(tail)

#Display - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

display(head)

#Insert at the beginning O(1)

def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display(head)

#Insert at end O(1)

def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)
    