from data import x

testing = False

data = (
    x
    if not testing
    else """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
)

split = data.split("\n\n")
ranges = list(filter(None, split[0].split()))

def overlapped(r1, r2, tf, list_=None):
    if tf:
        return max(r1[0], r2[0]) <= min(r1[1], r2[1])
    list_.append(f"{min(r1[0], r2[0])}-{max(r1[1], r2[1])}")

def parseInput(r1, r2=None):
    return (
        (int(r1.split("-")[0]), int(r1.split("-")[1])),
        (int(r2.split("-")[0]), int(r2.split("-")[1])) if r2 else "",
    )

tmp = []

p = 0

def checkAll():
    global ranges
    merged = []
    used = set()
    for i in range(len(ranges)):
        a,b = map(int, ranges[i].split("-"))
        for j in range(i+1, len(ranges)):
            r1,r2 = parseInput(ranges[i], ranges[j])
            if overlapped(r1,r2,True):
                overlapped(r1,r2,False, merged)
                used.add(i)
                used.add(j)
                break
        if i not in used:
            merged.append(ranges[i])
    ranges = merged
    return ranges


prev_len = -1
while prev_len != len(ranges):
    prev_len = len(ranges)
    ranges = checkAll()

p = 0
for r in ranges:
    start, end = map(int, r.split("-"))
    p += end - start + 1


print(p)
