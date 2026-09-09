class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, ival in enumerate(nums):
            for j, jval in enumerate(nums):
                if i != j and ival == jval: 
                    return True 
        return False