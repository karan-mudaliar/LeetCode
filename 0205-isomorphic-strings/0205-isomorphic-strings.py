class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = {}
        b = {}

        for x,y in zip(s,t):
            if x not in a:
                a[x] = y
            else:
                if a[x]!= y:
                    return False
            
            if y not in b:
                b[y] = x
            else:
                if b[y] != x:
                    return False

        return True
        