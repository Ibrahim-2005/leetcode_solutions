class Solution(object):
    def twoSum(self, nums, target):
        h={}
        for i in range(len(nums)):
            if nums[i] in h:
                return (h[nums[i]],i)
            else:
                h[target-nums[i]]=i

                