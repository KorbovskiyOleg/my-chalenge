# добавление элемента массива в ручную

class SimpleArray:
    def __init__(self):
        self.capacity  = 5 
        self.data = [None]* self.capacity

    def set(self,index, value):
        self.data[index]= value

    def get(self, index):
        return self.data[index]
    
    # методы которые изменяют объект не возвращают значений!!!!Запомним!!
    def reset(self):
        self.data = [None]*self.capacity 

sa = SimpleArray()
sa.set(1,'A')
sa.set(2, 'D')
sa.set(3, 'C')
sa.set(4, 'B')

print(sa.get(4))
print(sa.data)

sa.reset()
print(sa.data)
