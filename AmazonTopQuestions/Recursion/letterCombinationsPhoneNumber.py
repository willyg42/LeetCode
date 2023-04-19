def letterCombinations(self, digits: str) -> List[str]:
    digMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    results = []
    def dfs(rem, res):
        if rem == '':
            results.append(res)
            return
        for char in digMap[rem[0]]:
            dfs(rem[1:], res + char)
            
    if not digits:
        return []
    dfs(digits, '')
    return results