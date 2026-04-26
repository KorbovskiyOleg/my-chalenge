# функция для выведения суммы чисел в массиве в ООП стиле

class SimpleArray:
    
    def sum_num(self,num=[3]):
        total = 0
        for i in num:
            total+=i
        return total

sa = SimpleArray()
print(sa.sum_num([1,2,3]))
