class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary(n):
            count=0
            res=0
            for i in n[::-1]:
                res+=(2**count)*int(i)
                count+=1
            return res
        return bin(binary(a)+binary(b))[2:]
