class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = dict(sorted(c.items(), key = lambda item: item[1], reverse = True))

        return list(c.keys())[:k]