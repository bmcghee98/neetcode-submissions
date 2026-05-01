from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)

        for s in strs:
            label = "".join(sorted(s))
            buckets[label].append(s)

        return list(buckets.values())