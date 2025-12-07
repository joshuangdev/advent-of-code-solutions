from data import x

testing = False

input_data = (
    x
    if not testing
    else """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
)

inv = []

for criteria in input_data.split(","):
    startRange = int(criteria.split("-")[0])
    endRange = int(criteria.split("-")[1])
    p = []
    rinv = []
    for possibilities, index in enumerate(range(endRange-startRange+1), startRange):
        p.append(possibilities)
    #print(p)
    for entry in p:
        splitPoint = len(str(entry))//2
        one = str(entry)[:splitPoint]
        two = str(entry)[splitPoint:]
        if one==two:
            rinv.append(int(entry))
    inv.append(sum(rinv))

print(sum(inv))
