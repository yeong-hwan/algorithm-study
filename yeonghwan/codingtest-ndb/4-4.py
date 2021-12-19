from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
game_map = [list(map(int, input().split())) for i in range(N)]
answer = 0


def turn_left(direction):
    if direction == 0:
        return 3
    else:
        return direction - 1


def move(y, x, direction):
    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    else:
        x -= 1
    return y, x


d = turn_left(d)
next_y, next_x = move(y, x, d)
if game_map[next_y][next_x] == 0:
    game_map[next_y][next_x]
    y, x = next_y, next_x
    answer += 1
