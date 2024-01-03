class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2=set(nums)
        if(len(nums)>len(nums2)):
            return True
        else:
            return False