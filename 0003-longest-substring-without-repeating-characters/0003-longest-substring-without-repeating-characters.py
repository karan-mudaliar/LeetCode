class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0

        left = 0

        hashmap = {}

        for right in range(len(s)):
            if s[right] not in hashmap:
                length = max(length,right - left + 1)
            else:
                if hashmap[s[right]] < left:
                    length = max(length, right - left + 1)
                else:
                    left = hashmap[s[right]] + 1
            hashmap[s[right]] = right
        return length