from data import x

testing = False

data = (
    x
    if not testing
    else """987654321111111
811111111111119
234234234234278
818181911112111"""
)

result = []
fresult = []

def ListItemsstrToint(l:list):
    nl = []
    for entry in l:
        nl.append(int(entry))
    return nl

for line in data.split():
    currline = ListItemsstrToint(list(line))
    currline_length = len(currline)
    currentResult = []
    start = 0

    for times in range(12):
        runningLargest = 0
        runningLargest_index = start
        digits_remaining = 12 - times
        end = currline_length - digits_remaining + 1

        for i in range(start, end):
            if currline[i] > runningLargest:
                runningLargest = currline[i]
                runningLargest_index = i

        currentResult.append(runningLargest)
        start = runningLargest_index + 1

    result.append(currentResult)

for line in result:
    newline = ""
    for char in line:
        newline = f"{newline}{char}"
    fresult.append(int(newline))

print(fresult)
print(sum(fresult))
