class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count_each_frequency = [0] * len(nums)
        for start, end in requests:
            count_each_frequency[start] += 1
            if (end + 1) < len(nums):
                count_each_frequency[end + 1] -= 1
        
        for i in range(1, len(count_each_frequency)):
            count_each_frequency[i] += count_each_frequency[i - 1]
        prefix = count_each_frequency.copy() #copy for later use

        index_map = defaultdict(list) #freq:index
        for i in range(len(count_each_frequency)):
            freq = count_each_frequency[i]
            index_map[freq].append(i)
        nums.sort()
        count_each_frequency.sort()
        res = [0] * len(nums)
        for i in range(-1, -(len(nums) + 1), -1):
            index = index_map[count_each_frequency[i]].pop()
            res[index] = nums[i]
        summ = 0

        for i in range(len(res)):
            summ += (res[i] * prefix[i])
        return summ % (10**9 + 7)



        