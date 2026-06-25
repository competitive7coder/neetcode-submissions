class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        for f in range(s+1, len(nums)):
            if nums[s] != nums[f]:
                s+=1
                nums[s] = nums[f]
            else:
                f+= 1
        return s+1