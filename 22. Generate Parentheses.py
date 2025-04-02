from typing import List
from collections import Counter

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        full_len = 2 * n

        def is_valid(path: str) -> bool:
            count_each = Counter(path)
            if count_each['('] < count_each[')']:  # More ')' than '(' at any point
                return False
            if count_each['('] > n:  # More '(' than allowed
                return False
            return True

        def dfs_backtrack(start_idx, path):
            if start_idx == full_len:  # Valid sequence completed
                res.append("".join(path))
                return  

            for edge in ['(', ')']:  # Instead of get_edges()
                path.append(edge)
                
                # Validate before recursing
                if is_valid(path):
                    dfs_backtrack(start_idx + 1, path)

                path.pop()  # Backtrack

        dfs_backtrack(0, [])
        return res



##### this is a better run time version:
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, open_count, close_count):
            # Base case: If the length of the path is 2 * n, we have a valid sequence
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            # Add '(' if we haven't used all `n` opening brackets
            if open_count < n:
                path.append('(')
                backtrack(path, open_count + 1, close_count)
                path.pop()  # Backtrack

            # Add ')' if we haven't closed more than opened brackets
            if close_count < open_count:
                path.append(')')
                backtrack(path, open_count, close_count + 1)
                path.pop()  # Backtrack

        # Start backtracking
        backtrack([], 0, 0)
        return res
