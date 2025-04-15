### my not working version:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return []

        candidates.sort(reverse=True)
        print(candidates)
        n = len(candidates)

        memo = {}
        res = []

        # a_lst = [3, 2, 2]
        # b_lst = [2, 2, 3]

        # if a_lst == b_lst:
        #     print("true")
        # exit()

        def dfs_backtrack(idx, curr_sum: int, path: List[int]):

            if curr_sum ==  target:
                path.sort()
                if path not in res:
                    res.append(path[:]) # you need to add a deep copy
                    # print("res", res)
                return 

            if curr_sum > target:
                return 

            # if curr_sum in memo:
            #     return memo[curr_sum]

            # curr_sum = 0

            for i in range(n):
                #add pruning if applicable:
                if i > 0 and candidates[i-1] == candidates[i]:
                    continue

                if candidates[i] > target:
                    continue
                # edge = candidates[i] 
                path.append(candidates[i] )
                # curr_sum += candidates[i] 
                curr_sum = sum(path[:])
                # print("path, curr_sum", path, curr_sum)
                dfs_backtrack(i+1, curr_sum, path[:])
                    # curr_sum += edge

                path.pop()
            
            memo[curr_sum] = curr_sum
            return curr_sum

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


        dfs_backtrack(0, 0, [])
        print("res", res)
        return res
