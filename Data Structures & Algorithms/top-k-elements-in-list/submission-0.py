from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = Counter(nums)
        ans = seen.most_common(k)
        t_ans = [num for num, count in ans]
        return sorted(t_ans)