class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        total=numbers[start]+numbers[end]
        while(total!=target):
            if total>target:
                total=total-numbers[end]+numbers[end-1]
                end-=1  
            else:
                total=total-numbers[start]+numbers[start+1]
                start+=1
        return [start+1,end+1]