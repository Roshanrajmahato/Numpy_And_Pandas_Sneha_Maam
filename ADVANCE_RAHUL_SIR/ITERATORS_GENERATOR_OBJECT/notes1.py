 """   
Explicit Implimentation of range() method for 1 to 10 natuaral number
"It should contain __iter__() Method, __next__() Method"
"""
class numbers:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            if self.num<=10:
                res=self.num
                self.num+=1
                return res
            else:
                raise StopIteration
        except StopIteration :
            return "End of Iteration"
        
n1=numbers()

print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
