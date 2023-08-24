class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        ret = []
        def per(count = 1):
            if len(comb) == k:
                ret.append(comb.copy())
                return
            for i in range(count ,n + 1):
                comb.append(i)
                per(i + 1)
                comb.pop()
        per()
        return ret