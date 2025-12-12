from data import x
import math

testing = False

data = (
    x
    if not testing
    else """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """
)
horizontal = len(data.split("\n"))
# splitHorizontal = data.split("\n") # [::len(data.split("\n"))-1]\
rows = data.split("\n")
vertical = len(data.split())//horizontal
splitVertical = data.split()
questions = { str(i): [] for i in range(vertical) }
for que in questions:
    q = int(que)
    for row in rows:
        r = row.split()
        questions[str(que)].append(r[q])
r=[]
for _ in questions:
    sym = questions[_][len(questions[_])-1]
    questions[_].pop()
    if sym == "*":
        v = math.prod(int(i) for i in questions[_])
        r.append(v)
    elif sym == "+":
        v = sum(int(i) for i in questions[_])
        r.append(v)
print(sum(r))



