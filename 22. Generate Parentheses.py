from collections import Counter



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = [] # note: each path should be str and the return statement should be [str].
        full_len = 2 * n
        full_input = '()' * n
        print(full_input)

        def is_valid(edge: str):
            count_each = Counter(edge)
            print(count_each, count_each['('])
            if count_each['('] < count_each[')']:
                return False

            if count_each['('] > n:
                return False

            return True

        def dfs_backtrack(start_idx, path,):
            
            if len(path) == full_len: # when we reach a leaf node
                res.append("".join(path))
                print("res", res)
                return # always return blank in backtracking

            for edge in get_edges(start_idx):
                if not is_valid(edge):
                    continue

                path.append(edge)
                print("path", path)
                # if additional states:
                #     update(...additional states)
                dfs_backtrack(start_idx + len(edge), path)
                path.pop() ## revert(...additional states) if necessary e.g. permutations. 


        # edge = '())'
        # print(is_valid(full_input))

        dfs_backtrack(0, [])
        return res
        
