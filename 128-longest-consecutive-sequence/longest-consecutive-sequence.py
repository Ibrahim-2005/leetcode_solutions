class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        if not nums:
            return 0
        maxlen=1
        current=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i] == nums[i-1] +1:
                current+=1
            else:
                current=1
            maxlen=max(maxlen,current)
        return maxlen
            