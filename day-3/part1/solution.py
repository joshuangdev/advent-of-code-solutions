from data import x

testing=False

data = x if not testing else """987654321111111
811111111111119
234234234234278
818181911112111"""

r =[]

for line in data.split():
    currline = list(line)
    ind = 0
    b = None
    lrg = 0
    for char in currline:
        ind += 1
        if ind == len(currline):
            break
        if int(char) > lrg:
            b = (int(char) , ind)
            lrg = int(char)
    for i in range(b[1]):
        currline.pop(0)
    st = lrg
    lrg = 0
    for char in currline:
        if int(char) > lrg:
            lrg = int(char)
    r.append(int(f"{st}{lrg}"))

print(sum(r))





