import json
import sys

class Rule:
    def __init__(self, base, neighbour, dir):
        self.base = base
        self.neighbour = neighbour
        self.dir = dir
    
    def __repr__(self) -> str:
        return f"legal({self.dir[0]}, {self.dir[1]}, {self.base}, {self.neighbour})."
    
    def __hash__(self):
        return hash(self.__repr__())
    
    def __eq__(self, other):
        return (isinstance(other, Rule) and
                (self.base == other.base) and 
                (self.neighbour == other.neighbour) and 
                (self.dir == other.dir))

# file_name = "input.json"
file_name = sys.argv[1]
f = open(file_name)
data = json.load(f)

rules = set()
patterns = set()

grid = data["sample"]
height = len(grid)
width = len(grid[0])


for i in range(len(grid)):
    for j in range(len(grid[i])):

        patterns.add(grid[i][j])

        # for k in range(-1, 2):
        #     for l in range(-1, 2):
        #         dx = (i+k)%width
        #         dy = (j+l)%height
        #         rules.add(Rule(grid[i][j], grid[dx][dy], (k, l)))
            

        # rules.add(Rule(grid[i][j], grid[(i-1)%width][j], (0, -1)))
        # rules.add(Rule(grid[i][j], grid[(i+1)%width][j], (0, 1)))
        # rules.add(Rule(grid[i][j], grid[i][j], (0, -1)))
        # rules.add(Rule(grid[i][j], grid[(i-1)%width][j], (0, -1)))

        if i - 1 >= 0:
            rules.add(Rule(grid[i][j], grid[i-1][j], (0, -1)))
        if i + 1 < width:
            rules.add(Rule(grid[i][j], grid[i+1][j], (0, 1)))
        if j - 1 >= 0:
            rules.add(Rule(grid[i][j], grid[i][j-1], (-1, 0)))
        if j + 1 < height:
            rules.add(Rule(grid[i][j], grid[i][j+1], (1, 0)))

        if i - 1 >= 0 and j - 1 >= 0:
            rules.add(Rule(grid[i][j], grid[i-1][j-1], (-1, -1)))
        if i + 1 < width and j - 1 >= 0:
            rules.add(Rule(grid[i][j], grid[i+1][j-1], (1, -1)))
        if i - 1 >= 0 and j + 1 < height:
            rules.add(Rule(grid[i][j], grid[i-1][j-1], (-1, 1)))
        if i + 1 < width and j + 1 < height:
            rules.add(Rule(grid[i][j], grid[i-1][j-1], (1, 1)))
        

f = open(f"src/{data['file_name']}.lp", "w")

output = "#program rules.\n"
output += "\n".join(map(lambda rule: rule.__repr__(), rules))
output += "\n\n" + "\n".join([f"pattern({s})." for s in patterns])
print(output)

f.write(output)
f.close()