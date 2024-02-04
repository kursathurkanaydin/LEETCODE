class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        while len(nums[start:end+1])>2:
            mid=(start+end)//2
            son=nums[mid]
            if target==son:
                return mid
            elif target>son:
                start=mid+1
            else:
                end=mid-1
        if len(nums[start:end+1])==2:
            if target==nums[start:end+1][0]:
                return start
            elif target==nums[start:end+1][1]:
                return end
            elif target<nums[start:end+1][0]:
                return start
            elif target>nums[start:end+1][1]:
                return end+1
            else:
                return end
        mid=(start+end)//2
        if target==nums[mid]:
            return mid
        elif target>nums[mid]:
            return mid+1
        else:
            return mid  