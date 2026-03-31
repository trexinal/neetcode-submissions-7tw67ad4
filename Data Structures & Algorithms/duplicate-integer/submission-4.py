class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for i in range(len(nums)):
            if nums[i] in elems:
                return True
            else:
                elems.add(nums[i])
                print(elems)
        return False