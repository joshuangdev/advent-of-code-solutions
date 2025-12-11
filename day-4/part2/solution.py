from data import x

testing = False

input_data = (
    x
    if not testing
    else """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
)

grid = input_data.split()
f=0

def findNeighbour():
    for line_index, line in enumerate(grid):
        for paper_index, paper in enumerate(line):
            if paper != "@":
                continue

            counter = 0

            above_index = line_index - 1 if line_index - 1 >= 0 else None
            below_index = line_index + 1 if line_index + 1 < len(grid) else None
            left = paper_index - 1 >= 0
            right = paper_index + 1 < len(line)

            possibilities = [
                grid[above_index][paper_index] if above_index is not None else None,
                grid[above_index][paper_index + 1] if above_index is not None and right else None,
                grid[above_index][paper_index - 1] if above_index is not None and left else None,
                grid[below_index][paper_index] if below_index is not None else None,
                grid[below_index][paper_index + 1] if below_index is not None and right else None,
                grid[below_index][paper_index - 1] if below_index is not None and left else None,
                line[paper_index + 1] if right else None,
                line[paper_index - 1] if left else None,
            ]

            for pos in possibilities:
                if pos == "@":
                    counter += 1


            if counter < 4:
                return (line, line_index, paper_index)
    return (False, False, False)

while True:
    line, line_index, paper_index = findNeighbour()
    if not any([line, line_index, paper_index]):
        break
    else:
        f+=1
        grid[line_index] = f"{grid[line_index][0:paper_index]}.{grid[line_index][paper_index+1::]}"

