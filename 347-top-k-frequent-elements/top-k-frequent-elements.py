from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        count=Counter(nums)
        result_dict=(sorted(count.items(), key=lambda item:item[1],reverse=True))
        result=[]
        for i in range(k):
            result.append(result_dict[i][0])
        return result
