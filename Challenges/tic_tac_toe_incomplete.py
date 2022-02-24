def grid_creator(rows,cols):
    grid = []
    row = []
    
    for i in range(cols): #creates the columns
        row.append("🔲")
    
    for i in range(rows): #creates the rows
        grid.append(row)
        
    return grid
grid = grid_creator(3,3)

for row in grid:
    print(*row)
    
def turn(grid, player):
    for row in grid:
        print(*row)
    print("Please choose a square to place your symbol")
    row = int(input("Please enter your row number: "))
    col = int(input("Please enter your col number: "))
    grid[row][col] = "🐐"
    print("Updated game board: ")
    for row in grid:
        print(*row)
    
# Game loop:  
game_over = False
while game_over == False:
    print("Welcome to Tic-Tac-Toe: Founders Edition")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    player_1_symbol = "❌"
    player_2_symbol = "⭕"
    turn(grid,player1_name)
    game_over = True

    
