# создание динамического массива с ручным выделение памяти

class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.data = [None]*self.capacity
        self.length =0

    def append(self, value):
        if (self.capacity == self.length):
            self.capacity *=2
            
            new_data = [None]*self.capacity
            for i in range(self.length):
                new_data[i] = self.data[i]
            self.data = new_data


        self.data[self.length] = value
        self.length +=1

da = DynamicArray()
da.append('a')
da.append('b')
da.append('c')
da.append('d')
da.append('e')
da.append('f')
da.append('g')
da.append('h')
da.append('i')

print(da.data)
