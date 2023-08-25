class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [False for _ in range(len(s)+1)]
        arr[0] = True

        for idx in range(len(arr)):
            for start in range(idx):
                if arr[start] and s[start:idx] in wordDict:
                    arr[idx] = True
        return arr[-1]