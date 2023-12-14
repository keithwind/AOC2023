import re

with open("input.txt") as f:
    sum = 0
    mat = [list(x) for x in f.readlines()]
    length = len(mat)
    for i,l in enumerate(mat):
        s = "".join(l)
        matches = re.finditer(r"[0-9]+",s)
        for match in matches:
            a,b = match.span()
            a = a-1 if a > 0 else a
            b = b+1 if b < len(l) - 1 else b
            ss = []
            if i == 0:
                ss = mat[i+1][a:b] + [mat[i][a]] + [mat[i][b-1]]
            elif i == length - 1:
                ss = mat[i-1][a:b] + [mat[i][a]] + [mat[i][b-1]]
            else:
                ss = mat[i+1][a:b] + mat[i-1][a:b] + [mat[i][a]] + [mat[i][b-1]]
            for c in ss:
                if c != '.' and not c.isdigit():
                    sum += int(match.group())
                    break
    print(sum)
        
            