# найдем длину списка в LinkedList

class LinkedNode:
    def __init__(self, value):
        self.value = value
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

# реализуем метод delete

def delete(head,target):
    if head is None:
        return None
    if head.value == target:
        head = head.next

    return head

head = LinkedNode(12)
n2 = LinkedNode(1)
n3 = LinkedNode(2)
n4 = LinkedNode(3)

head.next = n2
n2.next = n3
n3.next  = n4

print(search(head))
head = delete(head,12)
print(head.value)







