class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        n = len(nums)
        def dfs_backtrack(start_idx, path):
            if start_idx == n:
                res.append(path) # note: path here is a list. 
                return # backtracking always return blank. 
            get_edges = nums
            for edge in get_edges(start_idx):

                #if pruning is needed?

                path.add(edge)
                dfs_backtrack(start_idx + len(edge), path[:])
                path.pop()

        dfs_backtrack(0, [])
        return res
