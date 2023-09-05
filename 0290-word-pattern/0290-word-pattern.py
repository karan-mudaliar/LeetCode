class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        H1 = {}
        H2 = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for x,y in zip(pattern,words):
            if x not in H1:
                H1[x] = y
            if y not in H2:
                H2[y] = x
            
            if H1[x] != y or H2[y] != x:
                return False

        
        return True