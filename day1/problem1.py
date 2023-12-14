with open("input.txt") as f:
    lines = f.readlines()
    num1 = []
    num2 = []
    for line in lines:
        for i in line:
            if i.isdigit():
                num1.append(i)
                break
        for i in line[::-1]:
            if i.isdigit():
                num2.append(i)
                break 
    sum = sum(map(int,num1))*10 + sum(map(int,num2))
    print(sum)

