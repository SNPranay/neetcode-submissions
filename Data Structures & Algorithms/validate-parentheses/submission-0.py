class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for c in s:
            if c in {'(', '{', '['}:
                res.append(c)
            else:
                if len(res) <= 0:
                    return False
                if c == ')':
                    if res[-1] == '(':
                        res.pop(-1)
                    else:
                        return False
                elif c == '}':
                    if res[-1] == '{':
                        res.pop(-1)
                    else:
                        return False
                elif c == ']':
                    if res[-1] == '[':
                        res.pop(-1)
                    else:
                        return False
        return len(res) == 0