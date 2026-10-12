class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0 
        self.vector = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.vector[i]

    def set(self, i: int, n: int) -> None:
        self.vector[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
            
        # insert at next empty position
        self.vector[self.length] = n
        self.length += 1
    def popback(self) -> int:
        temp = 0
        if self.length >0:
            self.length -= 1
            temp = self.vector[self.length]
            return temp

    def resize(self) -> None:
        temp = self.capacity
        self.capacity *= 2
        self.vector = self.vector + [0]*temp

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
