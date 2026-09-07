class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        n = len(tokens)

        for i in range(n):
            if tokens[i] not in {'+', '-', '/', '*'}:
                s.append(tokens[i])
            else:
                v2 = int(s.pop())
                v1 = int(s.pop())

                if tokens[i] == "+":
                    v = v1+v2
                elif tokens[i] == "-":
                    v = v1-v2
                elif tokens[i] == "/":
                    v = v1/v2
                else:
                    v = v1*v2

                s.append(v)
        return int(s[0])