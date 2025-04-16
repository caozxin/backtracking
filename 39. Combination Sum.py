### my slow but working version:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return []

        candidates.sort(reverse=True)
        n = len(candidates)

        memo = {}
        res = []

        def dfs_backtrack(idx, curr_sum: int, path: List[int]):

            if curr_sum ==  target:
                path.sort()
                if path not in res:
                    res.append(path[:]) # you need to add a deep copy
                return 

            if curr_sum > target:
                return 

            for i in range(n):
                #add pruning if applicable:
                if i > 0 and candidates[i-1] == candidates[i]:
                    continue

                if candidates[i] > target:
                    continue

                path.append(candidates[i] )
                curr_sum = sum(path[:])
                dfs_backtrack(i+1, curr_sum, path[:])
                path.pop()
            
            memo[curr_sum] = curr_sum
            return curr_sum

        dfs_backtrack(0, 0, [])
        return res
        
### improved working version:
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()
        res = []

        def dfs(idx: int, curr_sum: int, path: List[int]):
            if curr_sum == target:
                res.append(path[:])
                return
            if curr_sum > target:
                return

            for i in range(idx, len(candidates)):
                # You can reuse the same number, hence dfs(i, ...)
                path.append(candidates[i])
                dfs(i, curr_sum + candidates[i], path)
                path.pop()

        dfs(0, 0, [])
        return res


### best working version similar to my previous version:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return []

        candidates.sort(reverse=True)
        n = len(candidates)

        res = []

        def dfs_backtrack(idx, curr_sum: int, path: List[int]):

            if curr_sum ==  target:
                res.append(path[:])
                return 

            if curr_sum > target:
                return 

            for i in range(idx, n): #--> We dedup in the for loop by only using candidate numbers whose index in the array is >= last used number's index.
                #add pruning if applicable:
                if candidates[i] > target:
                    continue

                path.append(candidates[i] )
                dfs_backtrack(i, curr_sum + candidates[i], path)
                path.pop()

            return 

        dfs_backtrack(0, 0, [])
        return res
