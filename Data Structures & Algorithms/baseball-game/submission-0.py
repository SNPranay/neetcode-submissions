class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in range(len(operations)):
            if operations[i] == "+":
                s1 = res[-1]
                s2 = res[-2]
                res.append(s1+s2)
            elif operations[i] == "D":
                res.append(res[-1]*2)
            elif operations[i] == "C":
                res.pop(-1)
            else:
                res.append(int(operations[i]))
        
        return sum(res)
        