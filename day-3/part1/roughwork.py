from data import x

testing=True

data = x if not testing else """987654321111111
811111111111119
234234234234278
818181911112111"""

o = "348934838428883235888"
y = list(o)
ind = 0
b = None
lrg = 0
for char in y:
    ind +=1
    if int(char) > lrg:
        b = (int(char) , ind)
        lrg = int(char)
print(b)
for i in range(b[1]):
    y.pop(0)
print(y)
st = lrg
lrg = 0
for char in y:
    if int(char) > lrg:
        lrg = int(char)
print(int(f"{st}{lrg}"))





