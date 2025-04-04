### the 1st backtracking problem I solved by myself!!!
### my version: 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        n = len(nums)
        def dfs_backtrack(start_idx, path):
            if start_idx == n:
                res.append(path) # note: path here is a list. 
                # print("res", res)
                return # backtracking always return blank. 
            # get_edges = nums

            for edge in nums:
                #if pruning is needed:
                if edge in path:
                    continue
                # if not is_valid(edge):
                #     continue
                # print(edge, path)
                path.append(edge)
                # print("reset", nums[start_idx:])
                # exit()
                dfs_backtrack(start_idx + 1, path[:]) #len(edge)
                # print(path)
                path.pop()
                
                # exit()


        dfs_backtrack(0, [])
        return res
