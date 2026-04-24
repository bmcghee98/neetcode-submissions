from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        sp = sorted(freq.items(), key=lambda p: p[1], reverse=True)

        return [p[0] for p in sp[:k]]