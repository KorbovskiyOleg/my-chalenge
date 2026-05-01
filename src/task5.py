# Linked List

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# создаем три узла вручную
n1 = ListNode(10)
n2 = ListNode(20)
n3 = ListNode(30)

n1.next = n2
n2.next = n3

# проходим по цепочке

curr = n1
step = 0

while curr is not None:
    print(f"шаг: {step}, значение: {curr.value}")
    #curr = curr.next
    step +=1 # по правидам ставим счетчик перед сдвигом указателя
    curr = curr.next



    
