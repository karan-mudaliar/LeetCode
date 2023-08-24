class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ret = []

        def help (candidates,target,arr = []):
            if target == 0:
                ret.append(arr[:])
                return
            if target < 0:
                return

            for candidate in candidates:
                if not arr or candidate <=arr[-1]:
                    arr.append(candidate)
                    help(candidates,target - candidate,arr)
                    arr.pop()
        help(candidates,target)
        return ret

            