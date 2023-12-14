import re
s =0
key = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0
}
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        num = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))",line)
        s += key[num[0]]*10 + key[num[-1]]
    print(s)