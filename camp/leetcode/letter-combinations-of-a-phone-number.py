class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        ans = []
        path = []
        def backtrack(left):
            if len(path) == len(digits):
                ans.append("".join(path))
                return

            curr_cand = int(digits[left])
            for i in range(len(letters[curr_cand])):

                path.append(letters[curr_cand][i])

                backtrack(left+1)

                path.pop()
        backtrack(0)
        return ans