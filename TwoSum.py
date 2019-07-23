class Solution:
    def twoSum(self, nums, target):
                # Approach one 低效
        dic = {}
        length = len(nums)
        for i in range(length):
            dic[nums[i]] = i

        for i in range(length):     # 考虑一个target由两个相同的数字组成。例如[3,3] 6
            res =  target - nums[i]
            if res in dic.keys() and dic.get(res) != i:
                return [i, dic.get(res)]

s=Solution()
print(s.twoSum((1,3,4,6),10))