class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            diff_num = target - nums[i]
            if diff_num in diff:
                return [min(i, diff[diff_num]), max(i, diff[diff_num])]
            else:
                diff[nums[i]] = i
        return [] 

            