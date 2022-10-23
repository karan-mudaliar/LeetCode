class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf')]*(amount+1)
        arr[0] = 0
        
        for coin in coins:
            for amt in range(amount+1):
                if amt >= coin:
                    arr[amt] = min(arr[amt],1+arr[amt-coin])
        return arr[amount] if arr[amount] != float('inf') else -1
        