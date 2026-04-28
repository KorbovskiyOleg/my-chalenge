# создпние динамического массива

class DynamicArray:
    def __init__(self, capacity = 5):
        self.clean_capacity = capacity # вводим переменную для начального состояния мощности
        self.capacity = self.clean_capacity
        self.data = [None]* self.capacity
        self.length = 0

    def append(self,value):

        if(self.capacity ==self.length):
            self.capacity *=2

            new_data = [None]*self.capacity
            for i in range(self.length):
                new_data[i] = self.data[i]
            
            self.data = new_data

        self.data[self.length]= value
        self.length +=1

    def reset(self):
        self.data = [None]*self.clean_capacity
        self.length =0

da = DynamicArray()
da.append('a')
da.append('b')
da.append('c')
da.append('v')
da.append('g')
da.append('g')
da.append('o')
da.append('b')
da.append('r')

print(da.data)
da.reset()
print(da.data)


