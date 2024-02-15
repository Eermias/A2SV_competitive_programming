class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(list) #val:[index]
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] += [1, i, i]
            else:
                hashMap[nums[i]][0] += 1
                hashMap[nums[i]][1] += i
                hashMap[nums[i]].append(i)
        keys = hashMap.keys()
        res = [0] * len(nums)
        for item in keys:
            iteration = hashMap[item][0]
            total = hashMap[item][1]
            prefix = 0
            for i in range(iteration):
                num = hashMap[item][i + 2]
                prefix += num
                left_sum = (num * (i)) - (prefix - num)
                right_sum = (total - prefix) - (num * (iteration - i - 1))
                res[num] = left_sum + right_sum
        return res


        