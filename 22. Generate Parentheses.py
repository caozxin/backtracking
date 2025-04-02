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
