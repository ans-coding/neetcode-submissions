class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dlist = [0]*capacity
        self.length = 0
        self.capacity=capacity

    def get(self, i: int) -> int:
        return self.dlist[i]


    def set(self, i: int, n: int) -> None:
        self.dlist[i]=n


    def pushback(self, n: int) -> None:
        if (self.length == self.capacity):
            self.resize()
        self.dlist[self.length] = n
        self.length += 1
        


    def popback(self) -> int:
        if (self.length > 0):
            self.length-=1
            l = self.length
            return self.dlist[l]
 

    def resize(self) -> None:
        self.capacity *= 2
        nl = [0]*self.capacity
        for i in range(self.length):
            nl[i] = self.dlist[i]
        self.dlist = nl

    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
