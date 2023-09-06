class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_map = {
            "2" : 'abc',
            "3" : 'def',
            "4" : 'ghi',
            "5" : 'jkl',
            "6" : 'mno',
            "7" : 'pqrs',
            "8" : 'tuv',
            "9" : 'wxyz'
        }
        res = []

        def yelp(idx, string = ""):
            if len(string) == len(digits):
                res.append(string)
                return
            
            else:
                for char in dig_map[digits[idx]]:
                    yelp(idx + 1, string + char)
        if digits:
            yelp(0)
        return res

        