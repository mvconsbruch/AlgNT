# solutions2.py

def eq1(x1, x2, y1, y2):
    return (x1*x1 + 2*x2*x2 - 2*(x1*y2 + x2*y1) - y1*y1 - 2*y2*y2) % 4
def eq2(x1, x2, y1, y2):
    return (2*(x1*x2 - y1*y2) - x1*y1 - 2*x2*y2) % 4

solutions_found = False
for x1 in range(4):
    for x2 in range(4):
        for y1 in range(4):
            for y2 in range(4):
                if x1%2 == 0 and x2%2 == 0 and y1%2 == 0 and y2%2 == 0: 
                    continue
                if eq1(x1,x2,y1,y2) == 0 and eq2(x1,x2,y1,y2) == 0:
                    solutions_found = True
                    print(f"Solution found! (x1,x2,y1,y2) = ({x1},{x2},{y1},{y2})")

if solutions_found == False:
    print("no")
