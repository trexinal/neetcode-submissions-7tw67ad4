class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sort = set()
        for num in nums:
            if num in sort:
                return True
            sort.add(num)
        return False