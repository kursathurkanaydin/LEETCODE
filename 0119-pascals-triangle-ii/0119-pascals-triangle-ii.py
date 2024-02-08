class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    
        rep=[[1]]
        i=1
        while(i<=rowIndex):
            l=[1]
            for a in range(len(rep[i-1])-1):
                l.append(rep[i-1][a]+rep[i-1][a+1])
            l.append(1)
            rep.append(l)
            i+=1

        return rep[-1]