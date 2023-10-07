class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        if len(s) == 0:
            return True
        
        for char in t:
            
            if s[idx] == char:
                idx +=1
                if idx == len(s):
                    return True
        return idx == len(s)