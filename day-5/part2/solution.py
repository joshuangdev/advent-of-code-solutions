from data import x

testing=False

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
ranges = split[0].split()
#entries = split[1].split()
#fresh = 0
#print(ranges,entries)

for _ in ranges:
    startRange = int(_.split("-")[0])
    endRange = int(_.split("-")[1])
    if startRange <= igr <= endRange:
        fresh +=1

print(fresh)
