def solution(grid):
    answer = []
    cycle_len = 1
    row, col = 0, 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        if grid[row][col] == 'S':
        
        elif grid[row][col] == 'R':
        
        else:
        while row != 0 and col != 0:
            if 

    answer.sort()
    return answer


print(solution(["SL", "LR"]))
