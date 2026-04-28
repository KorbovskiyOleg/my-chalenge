# создпние динамического массива

class DinamicArray:
    def __init__(self):
        self.capacity = 5
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
        #self.length +=1

da = DinamicArray()
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


