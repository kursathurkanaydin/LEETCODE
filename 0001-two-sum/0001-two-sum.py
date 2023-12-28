class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=0
        for a in nums[:len(nums)-1]:
            y=x+1
            for b in nums[y:]:
                if(a+b==target):
                    dizi=[x,y]
                    return dizi
                else:
                    y+=1
            x+=1
    
