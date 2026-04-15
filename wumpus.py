size = 4

world = [["Safe" for _ in range(size)] for _ in range(size)]

pits = [(1,2),(2,2)]
wumpus = (3,1)

for p in pits:
    world[p[0]][p[1]] = "Pit"

world[wumpus[0]][wumpus[1]] = "Wumpus"
def neighbors(x,y):
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    cells=[]
    for dx,dy in moves:
        nx,ny=x+dx,y+dy
        if 0<=nx<size and 0<=ny<size:
            cells.append((nx,ny))
    return cells

def percept():
    breeze=set()
    stench=set()

    for x,y in pits:
        for n in neighbors(x,y):
            breeze.add(n)

    for n in neighbors(wumpus[0],wumpus[1]):
        stench.add(n)

    return breeze,stench


breeze, stench = percept()

print("Breeze Cells:", breeze)
print("Stench Cells:", stench)

print("\nWorld State")

for i in range(size):
    for j in range(size):
        print(world[i][j], end="\t")
    print()
