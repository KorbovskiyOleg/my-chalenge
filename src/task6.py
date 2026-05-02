# найдем длину списка в LinkedList

class LinkedNode:
    def __init__(self, value):
        self.head = value
        self.next = None

def search(head):
    curr = head
    index =0
    
    if curr == None:
        return 0
    while curr is not None:
        index +=1
        curr = curr.next

    return index

n1 = LinkedNode(12)
n2 = LinkedNode(1)
n3 = LinkedNode(2)
n4 = LinkedNode(3)

n1.next = n2
n2.next = n3
n3.next  = n4


print(search(n1))
