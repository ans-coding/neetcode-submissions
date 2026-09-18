class MinStack:

    def __init__(self):
        self.content = []

    def push(self, val: int) -> None:
        self.content.append(val)

    def pop(self) -> None:
        self.content.pop()

    def top(self) -> int:
        return(self.content[-1])

    def getMin(self) -> int:
        min1 = self.content[0]
        if len(self.content)>1:
            for i in range(1,len(self.content)):
                if self.content[i]<min1:
                    min1 = self.content[i]
        return min1
        
