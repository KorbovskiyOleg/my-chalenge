# создание динамического массива с ручным выделение памяти

class DynamicArray:
    def __init__(self, capacity = 5):
        self.initial_capacity = capacity
        self.capacity = self.initial_capacity
        self.data = [None]*self.capacity
        self.length =0
    
    def resize(self,new_capacity):
        if new_capacity == self.capacity:
            return
        if new_capacity <self.length:
            raise ValueError(f"размер new_capacity меньше чем длина массива")

            
        new_data = [None]*new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity


    def append(self, value):
        if self.capacity ==self.length:
            self.resize(self.capacity*2)


        self.data[self.length] = value
        self.length +=1

    def reset(self):
        self.data = [None]* self.initial_capacity
        self.length =0 

da = DynamicArray()
for x in 'abcdefckfjsd': da.append(x)

print(da.data)
#da.reset()
print(da.data)
da.resize(11)
print(da.data)








