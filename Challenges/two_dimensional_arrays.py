scores = [100.2, 50.1, 30.6, 500.4]
scores2 = [400.0, 300.1, 33, 2134]
scores3 = [4343, 55, 66, 1]

grid = [scores,scores2,scores3]

for row in grid:
    print(row)

print(grid[0][2]) # [row] [column] 

for row in grid:
    for column in row:
        print(column) # 2 loops (nested loops)
