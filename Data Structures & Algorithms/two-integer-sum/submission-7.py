class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i  in range(len(nums)):
        #     for j  in range(len(nums)):
        #         if i!=j:
        #             if nums[i] + nums[j] == target:
        #                 return [i, j]

        indices = {} # create hashmap

        for i, n in enumerate(nums):
            indices[n] = i # create hashmap
        
        for i, n in enumerate(nums):
            diff = target - n #compute diff of current element
            if diff in indices and indices[diff] != i: # does it exist?
                return [i, indices[diff]] #return
        return []

            