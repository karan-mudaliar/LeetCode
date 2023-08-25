class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf')] * (amount+1)
        arr[0] = 0
        for amt in range(1,amount+1):
            for coin in coins:
                if amt >= coin:
                    arr[amt] = min(arr[amt - coin] + 1, arr[amt])
        
        return arr[-1] if arr[-1] != float('inf') else -1
        
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         arr = [float('inf')]* (amount+1)
#         arr[0] = 0

#         for coin in coins:
#             for amt in range(1,amount+1):
#                 if amt >= coin:
#                     arr[amt] = min(arr[amt],1 + arr[amt-coin])
        
#         return arr[-1] if arr[-1] != float('inf') else -1

        
        