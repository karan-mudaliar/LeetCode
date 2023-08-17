class Solution:
    def longestPalindrome(self, s: str) -> str:

    
        def yelp(s,i,j):
            start = 0
            end = len(s) - 1
            print(i)
            while i >= start and j <= end:
                left = s[i]
                right = s[j]
                if left == right:
                    i -= 1
                    j += 1
                else:
                    break
            print(s[i-1:j])
            return ''.join(s[i+1:j])

        mstring = ""
        for i in range(len(s)):
            odd = yelp(s,i,i)
            even = yelp(s,i,i+1)
            mstring = max(mstring,odd,even, key = len)
        return mstring