class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] +=1
            return digits
        else:
            num = "".join([str(x)for x in digits])
            num = int(num)
            num += 1
            

        return [int(x) for x in str(num)]
