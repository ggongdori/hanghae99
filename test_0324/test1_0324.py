def solution(dirs):
    answer = 0
    #처음 걸어본 길이니까 set
    visited = set()
    #시작 좌표
    x, y = 0, 0
    for d in dirs:
        if d == 'U' and y < 5:
            visited.add(((x,y), (x, y+1)))
            y += 1
        elif d == 'D' and y > -5:
            visited.add(((x,y-1), (x, y)))
            y -= 1
        elif d == 'R' and x < 5:
            visited.add(((x, y), (x+1, y)))
            x += 1
        elif d == 'L' and x > -5:
            visited.add(((x-1, y), (x, y)))
            x -= 1
    return len(visited)