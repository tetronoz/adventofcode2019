def build_range(coords):
    ranges = [[(0,0), (0,0)]]
    for c in coords:
        if c[0] == 'R':
            x = ranges[-1][1][0] + int(c[1:])
            y = ranges[-1][1][1] 
            ranges.append([(ranges[-1][1][0],ranges[-1][1][1]), (x,y)])
        elif c[0] == 'L':
            x = ranges[-1][1][0] - int(c[1:])
            y = ranges[-1][1][1] 
            ranges.append([(ranges[-1][1][0],ranges[-1][1][1]), (x,y)])
        elif c[0] == 'D':
            x = ranges[-1][1][0]
            y = ranges[-1][1][1] - int(c[1:])
            ranges.append([(ranges[-1][1][0],ranges[-1][1][1]), (x,y)])
        elif c[0] == 'U':
            x = ranges[-1][1][0]
            y = ranges[-1][1][1] + int(c[1:])
            ranges.append([(ranges[-1][1][0],ranges[-1][1][1]), (x,y)])
    return ranges

def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    left = max(min(x1,x2),min(x3,x4))
    right = min(max(x1,x2),max(x3,x4))

    top = min(max(y1,y2),max(y3,y4))
    bottom = max(min(y1,y2),min(y3,y4))
    
    if left == right and bottom == top:
        return (right, top)
    else:
        return None

with open("../input/input.txt") as fp:
    line_num = 0
    for line in fp:
        coords = line.strip().split(',')
        if line_num == 0:
            range1 = build_range(coords)
        if line_num == 1:
            range2 = build_range(coords)
        line_num += 1
            
md = float("inf")
min_steps = float("inf")
wire1_steps = 0
for i in range(1, len(range1)):
    wire1_steps += abs(range1[i][0][0] - range1[i][1][0]) + abs(range1[i][0][1]-range1[i][1][1])
    d1 = range1[i][1]
    wire2_steps = 0
    for j in range(1, len(range2)):
        wire2_steps += abs(range2[j][0][0] - range2[j][1][0]) + abs(range2[j][0][1]-range2[j][1][1])
        d2 = range2[j][1]
        res = findIntersection(range1[i][0][0], range1[i][0][1], range1[i][1][0], range1[i][1][1], 
                         range2[j][0][0], range2[j][0][1], range2[j][1][0], range2[j][1][1])
        
        total_steps = wire1_steps + wire2_steps
        
        if res and res != (0,0):
            d1_to_res = abs(res[0] - d1[0]) + abs(res[1] - d1[1])
            d2_to_res = abs(res[0] - d2[0]) + abs(res[1] - d2[1])
    
            temp = abs(0 - res[0]) + abs(0 - res[1])
            md = min(md, temp)

            min_steps = min(min_steps, total_steps - d1_to_res - d2_to_res)
            
print(f"{md} - {min_steps}")