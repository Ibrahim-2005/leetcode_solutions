class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash={}
        for i in range(len(nums)):
            if target-nums[i] not in hash:
                hash[nums[i]]=i
            else:
                return (i,hash[target-nums[i]])
        