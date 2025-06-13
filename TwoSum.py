class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for i, value in enumerate(nums):
            dic[value] = i

        for i in range(len(nums)):
            check = target - nums[i]
            if check in dic:
                if i != dic[check]:
                    return [i, dic[check]]
