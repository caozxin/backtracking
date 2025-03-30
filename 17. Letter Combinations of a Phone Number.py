from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        len_of_solu = len(digits)
        # digits_lst = list(digits)
        # print(digits_lst)

        #mapping for num to letters:
        num_char = {
            '2': ['a','b', 'c'],
            '3': ['d', 'e', 'f']
        }
        KEYBOARD = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }


        def dfs_backtrack(start_idx:int, path:List[str]):

            if start_idx == len_of_solu:
                res.append("".join(path))
                # print("res: ", res)
                return 
            next_num = digits[start_idx] # the start_idx matches the order of the nums! 
            for letter in KEYBOARD[next_num]:
                path.append(letter)
                print(path)
                dfs_backtrack(start_idx + 1, path) # this traversal is pre-order == DFS
                path.pop()

        res = []

        dfs_backtrack(0,[])
        return res
