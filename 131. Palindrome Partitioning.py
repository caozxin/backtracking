class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs_backtrack(start_idx, path):
            if start_idx == n: # if the substring has the len of input string, then it reachs the leaf.
                if path is palindrome: 
                    res.append("".join(path))
                return # always return blank in backtracking. 

            for edge in get_edges(start_idx):
                if not is_subtring(edge):
                    continue

                path.add(edge)
                dfs_backtrack(start_idx + len(edge), path)
                path.pop()

        res = set() # avoid duplication. 
        dfs_backtrack(0, [])
        return res
