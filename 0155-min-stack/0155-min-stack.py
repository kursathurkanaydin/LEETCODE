class MinStack:

    def __init__(self):
        self.dizi=[]
        
    def push(self, val: int) -> None:
        self.dizi.append(val)


    def pop(self) -> None:
        self.dizi.pop()

    def top(self) -> int:
        top=self.dizi[-1]
        return top
    def getMin(self) -> int:
        deger=min(self.dizi)
        return deger
