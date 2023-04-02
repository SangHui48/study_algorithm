# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    x, y = 0, 0
    map = dict()
    for command in dirs:
        if command == 'U' and y < 5:
            map[(x, y, x, y + 1)] = True
            y += 1
        elif command == 'D' and -5 < y:
            map[(x, y-1, x, y)] = True
            y -= 1
        elif command == 'R' and x < 5:
            map[(x, y, x+1, y)] = True
            x += 1
        elif command == 'L' and x > -5:
            map[(x-1, y, x, y)] = True
            x -= 1
    return len(map)