class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def if_palindrome(word):
            return word == word[::-1]

        def dfs_backtrack(start, path):
            # print("  dfs")
            if start == n: # if the substring has the len of input string, then it reachs the leaf.
                # res.append("".join(path))
                res.append(path[:])
                return # always return blank in backtracking. 

            for end in range(start+1, n+1): #first you need to gather all defined edges, in this case substrings
                substr = s[start:end]
                # print(start, end, substr)
                # dfs_backtrack(end, path) # in each recursive call, end_idx pass in as start_idx
                if if_palindrome(substr):
                    # path.append(edge)
                    dfs_backtrack(end, path + [substr])
                    # path.pop() # this should be right after dfs(). 

        res = [] 
        dfs_backtrack(0, [])
        return res
