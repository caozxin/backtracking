from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        len_of_solu = len(digits)
        digits_lst = list(digits)
        print(digits_lst)

        #mapping for num to letters:
        num_char = {
            '2': ['a','b', 'c'],
            '3': ['d', 'e', 'f']
        }

        # print(num_char)
        # print(num_char['2'])

        def dfs_backtrack(start_idx:int, path:List[str]):
            if start_idx == len_of_solu:
                res.append("".join(path))
                print("res: ", res)
            return 

            for letter in num_char['2']:
                path.append(letter)
