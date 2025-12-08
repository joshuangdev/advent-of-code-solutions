from data import x
import re

testing = False

input_data = (
    x
    if not testing
    else """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
)

inv = []

def split_string_n_chars(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

for criteria in input_data.split(","):
    startRange = int(criteria.split("-")[0])
    endRange = int(criteria.split("-")[1])
    p = []
    rinv = []
    for possibilities, index in enumerate(range(endRange-startRange+1), startRange):
        p.append(possibilities)
    #print(p)
    for number in range(startRange, endRange + 1):
        match = re.match(r"^(.+)\1+$", str(number))
        if match:
            rinv.append(int(number))
    inv.append(sum(rinv))

print(sum(inv))
