class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) <=0:
            return s
        left = 0
        right = len(s) - 1
        string = [x for x in s]
        vowels = 'aeiouAEIOU' 

        while left <= right:

            while left <= right and string[left] not in vowels:
                left += 1
            while left <= right and string[right] not in vowels:
                right -= 1
            if left <= right:
                self.swap(string,left,right)
                left += 1
                right -= 1

        return ''.join(string)

    def swap(self,arr,i,j):
        arr[i], arr[j] = arr[j], arr[i]
        