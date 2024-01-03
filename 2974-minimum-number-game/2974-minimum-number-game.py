class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=list()
        i=0
        nums.sort()
        while(i<len(nums)):
            res.append(nums[i+1])
            res.append(nums[i])
            i+=2
        return res
            
            
            
            
        