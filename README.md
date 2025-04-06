![image](https://github.com/user-attachments/assets/24671d32-eb30-4e5d-ac16-5514a510c92d)

![image](https://github.com/user-attachments/assets/fcd259b3-ded8-46fc-a74e-3ec23a5ba05b)

![image](https://github.com/user-attachments/assets/bc3ffedf-7498-4ac3-a09b-e2a765c7025b)

Example to solve Combinatorial Search Problem:Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

  # Implement Backtracking: Draw the tree, draw the tree, draw the tree!!!


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

<img width="682" alt="image" src="https://github.com/user-attachments/assets/f46523dd-2142-429d-8e1c-e596cc02792f" />

<img width="655" alt="image" src="https://github.com/user-attachments/assets/fe7968cd-af01-45ee-aabf-dca6afc5ee20" />

  # Backtracking with Pruning Template:



    function dfs(start_index, path):
    if is_leaf(start_index):
       report(path)
       return
    for edge in get_edges(start_index):
      # prune if needed
      if not is_valid(edge):
        continue
      path.add(edge)
      # increment start_index
      dfs(start_index + len(edge), path)
      path.pop()

    dfs(0, []) #the start_idx always starts at 0
    return res

# state-space tree in Palindrome Partitioning example:
<img width="637" alt="image" src="https://github.com/user-attachments/assets/f9eaf11b-f964-4ee2-bf93-769faab9ee00" />

  <img width="641" alt="image" src="https://github.com/user-attachments/assets/ea7b5a76-c639-4bf8-b958-9569b03a00b8" />

    ans = []
    def dfs(start_index, path, [...additional states]):
        if is_leaf(start_index):
            ans.append(path[:]) # add a copy of the path to the result
            return
            
        for edge in get_edges(start_index, [...additional states]):
            if not is_valid(edge):  # prune if needed
                continue
            path.add(edge)
            
            if additional states:
                update(...additional states)
                
            dfs(start_index + len(edge), path, [...additional states])
            
            path.pop() # revert(...additional states) if necessary e.g. permutations
            
  # Backtracking with Aggregation & Memoization Template: 
  -->Basically We use backtracking to aggregate the return value from child recursive calls to parent and bubble them up. 

      function def dfs(start_index, [...additional states]):
      if is_leaf(start_index):
          return 1
      ans = initial_value
      for edge in get_edges(start_index, [...additional states]):
          if additional states: 
              update([...additional states])
          ans = aggregate(ans, dfs(start_index + len(edge), [...additional states]))
          if additional states: 
              revert([...additional states])
      return ans


      
<img width="559" alt="image" src="https://github.com/user-attachments/assets/a2c0ed83-9ab9-4b66-b54a-6ea9d17e8b74" />
<img width="642" alt="image" src="https://github.com/user-attachments/assets/de1b381e-1533-4af8-9fa0-50bc5c4a85e0" />

  # Memoization, Backtracking, & Dynamic Programming: 
  <img width="892" alt="image" src="https://github.com/user-attachments/assets/bb443e53-e0ce-4533-bbce-9523071eb193" />

  <img width="857" alt="image" src="https://github.com/user-attachments/assets/787b8543-2d20-4bcd-88dd-8a0b7c519cdf" />
  
  <img width="867" alt="image" src="https://github.com/user-attachments/assets/4dbf3b85-072d-4c3e-b074-40bde8f566a1" />

  
