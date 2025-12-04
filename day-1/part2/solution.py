from data import x
hint = x

def is_negative(num):
    return num < 0

current = 50
whole = 0

for items in hint.split():
    calculating = int(items[1:])
    if items[0] == "L":
        whole += calculating//100
        if current == 0:
            whole -= 1
        current -= calculating % 100
        if is_negative(current):
            current = 100-(current*-1)
            whole += 1
        if current == 0:
            whole += 1

    elif items[0] == "R":
        current += calculating % 100
        whole += calculating // 100
        if current > 99:
            if current == 100:
                whole+=1
                current = 0
            else:
                extra = current-100
                whole+=1
                current = extra


print(whole)

