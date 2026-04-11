class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 1

            else:
                hashmap[num] += 1
        
        sorted_nums = sorted(hashmap.items(), key = lambda x : x[1], reverse = True)

        return [x for x,y in sorted_nums[:k]]

        