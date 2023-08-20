class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        H = {}

        for char in magazine:
            H[char] = H[char] + 1 if char in H else 1

        for letter in ransomNote:
            if letter not in H or H[letter] <= 0:
                return False
            else:
                H[letter] -= 1
        return True 