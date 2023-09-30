class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0 
        str1 = [x for x in word1]
        str2 = [x for x in word2]
        res = []

        while i < len(str1) and j < len(str2):
            res.append(str1[i])
            res.append(str2[j])
            i += 1
            j += 1
        
        res.extend(str1[i:])
        res.extend(str2[j:])
            
        return ''.join(res)