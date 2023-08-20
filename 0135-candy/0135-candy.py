class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1 for _ in ratings]

        for i in range(1,len(candy)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i-1] + 1
        
        print(candy)

        for i in reversed(range(len(candy)-1)):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i + 1]:
                candy[i] = candy[i+1]+1
        
        print(candy)

        return sum(candy)

        