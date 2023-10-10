class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf') for i in range(amount + 1)]

        arr[0] = 0

        for coin in coins:
            for amoun in range(amount + 1):
                if amoun - coin >= 0:
                    arr[amoun] = min(arr[amoun],arr[amoun - coin]+1)

        return arr[-1] if arr[-1] != float('inf') else -1

        
        