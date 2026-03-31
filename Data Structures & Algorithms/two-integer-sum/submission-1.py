class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            diff_num = target - nums[i]
            if diff_num in diff:
                small = min(i, diff[diff_num])
                large = max(i, diff[diff_num])
                result = [small, large]
                return result
            else:
                diff[nums[i]] = i
        return result 

            