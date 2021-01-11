import os
from colorama import Fore
states = [i for i in range(9)] # (or list(range(9) ) the state of the game
DEFAULT_STATES = states[:] # copy (create new) states for future checks
WIN_CHECKS = [ # win statas
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

is_first_player = True
is_finished = False
# this code is a great candidat to be put in function to obey DRY
BOARD = f"""
{states[0]} | {states[1]} | {states[2]} 
-----------
{states[3]} | {states[4]} | {states[5]} 
-----------
{states[6]} | {states[7]} | {states[8]}"""
os.system('cls' if os.name == 'nt' else 'clear')
print(BOARD)
# this code is a great candidat to be put in function to obey DRY

while not is_finished:
    if is_first_player: # config for current player
        sign = Fore.RED + "X" + Fore.RESET
        current_player = Fore.RED + "Player 1" + Fore.RESET
    else:
        sign = Fore.GREEN + "O" + Fore.RESET
        current_player = Fore.GREEN + "Player 2" + Fore.RESET
    while True:
        move = int(input(f"{current_player} Your move: "))
        if states[move] in DEFAULT_STATES: # check if the cell is available
            states[move] = sign
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    # this code is a great candidat to be put in function to obey DRY
    BOARD = f"""
    {states[0]} | {states[1]} | {states[2]} 
    -----------
    {states[3]} | {states[4]} | {states[5]} 
    -----------
    {states[6]} | {states[7]} | {states[8]}"""
    print(BOARD)
    # this code is a great candidat to be put in function to obey DRY
    for check_list in WIN_CHECKS: # cycle through win states and check every state
        if states[check_list[0]] == states[check_list[1]] == states[check_list[2]] == sign:
            print(f"{current_player} has won!", )
            is_finished = True # signal to while loop to stop
    available_cells = 0 # guess what nobody has won
    for cell in DEFAULT_STATES: # loop for every cell to check its state
        if states[cell] in DEFAULT_STATES:
            available_cells += 1 # increase available cells counter
    if available_cells == 0: # if the guess is correct - finish the game
        print("Nobody has won!")
        is_finished = True
    is_first_player = not is_first_player # if no one has won and there are more cells - swap the player
    
