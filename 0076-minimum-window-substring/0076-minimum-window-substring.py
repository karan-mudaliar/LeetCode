class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""

        countT, countS = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char,0)

        res, resLen = (-1,-1), float('inf')

        have, need = 0, len(countT)

        left = 0

        for right in range(len(s)):
            curr = s[right]
            countS[curr] = 1 + countS.get(curr,0)

            if curr in countT and countS[curr] == countT[curr]:
                have += 1
            
            while have == need:
                if resLen > (right - left + 1):
                    res = (left,right)
                    resLen = (right - left + 1)
                
                leftChar = s[left]
                countS[leftChar] -= 1

                if leftChar in countT and countS[leftChar] < countT[leftChar]:
                    have -= 1
                
                left += 1
        left,right = res

        return s[left:right+1] if resLen != float('inf') else ""


