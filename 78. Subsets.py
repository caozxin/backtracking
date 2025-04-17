class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # nums.sort()
        #none handling:
        if not nums:
            return [] # this should match with expected return format. 
        res = []
        n = len(nums)
        
        def dfs_backtrack(start_idx, path, res):

            # res.append(path[:])
            if sorted(path) not in res:

                res.append(sorted(path)[:])

            if start_idx == n: # this is if_leaf, but not where we want to update res[]
                return

            for i in range(start_idx, n):
                edge = nums[i]
                if edge in path:
                    continue
                path.append(edge)
                # res.add(path)
                print(path, edge)

                # if path.sort() in res:
                #     continue

                dfs_backtrack(start_idx+1, path, res)
                path.pop()

            # print(res, len(res))
            # exit()
    

        dfs_backtrack(0, [], res)
        print(res, len(res))
        return res
