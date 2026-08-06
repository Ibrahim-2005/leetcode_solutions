from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        sorted_dict=(sorted(Counter(nums).items(), key=lambda item: item[1],reverse=True))
        result=[]
        for i in range(k):
            result.append(sorted_dict[i][0])
        return result