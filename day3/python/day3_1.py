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
    if x3 < x1 < x4 and y1 < y3 < y2:
        return [x1, y3]
    elif x1 < x3 < x2 and y3 < y1 < y4:
        return [x3, y1]
    else:
        return 0,0

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
for i in range(1, len(range1)):
    if (0,0) in range1[i]:
        continue
    range1[i].sort()
    for j in range(1, len(range2)):
        if (0,0) in range2[j]:
            continue
        range2[j].sort()
        res = findIntersection(range1[i][0][0], range1[i][0][1], range1[i][1][0], range1[i][1][1], 
                         range2[j][0][0], range2[j][0][1], range2[j][1][0], range2[j][1][1])
        if res != (0,0):
            temp = abs(0 - res[0]) + abs(0 - res[1])
            md = min(md, temp)
print(md)