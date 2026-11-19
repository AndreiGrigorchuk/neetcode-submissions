class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value : i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] # prevMap[diff] index of the number, i is the index of the current number 
            prevMap[n] = i # prevMap[7] = 1 value(key) : index
        return 