class Solution:
    def letterCombinations(self, digits):
        alp_dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                    '8': "tuv", '9': "wxyz"}
        if not digits:
            return []
        comb = ['']
        for d in digits:
            comb = [p + q for p in comb for q in alp_dict[d]]
        return comb

