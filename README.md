![image](https://github.com/user-attachments/assets/24671d32-eb30-4e5d-ac16-5514a510c92d)

![image](https://github.com/user-attachments/assets/fcd259b3-ded8-46fc-a74e-3ec23a5ba05b)

![image](https://github.com/user-attachments/assets/bc3ffedf-7498-4ac3-a09b-e2a765c7025b)

Example to solve Combinatorial Search Problem:Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.




from typing import List

def letter_combination(n: int) -> List[str]:
    res: List[str] = []

    def dfs(start_index: int, path: List[str]) -> None:
        if start_index == n:
            res.append("".join(path))#only append all edges when it reachs leaf node
            print("res", res)
            return
        
        for letter in "ab": # here ab is each edge
            #if valid: 
            path.append(letter)
            print("path", path)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, []) #the start_idx always starts at 0
    return res

Another Template for Backtracking:
<img width="682" alt="image" src="https://github.com/user-attachments/assets/0d819dc1-2cdd-420b-a44f-d7feab5f1d27" />
