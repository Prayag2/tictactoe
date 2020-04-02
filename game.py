'''
Tic Tac Toe V2 Created By @PrayagJain12
'''

############################################################################################
# IMPORT
from time import sleep
from termcolor import colored
import os, sys

# VARIABLES
board_pos = list(' '*9)
used_pos = []
d_color = 'yellow'

# FUNCTIONS
def clear(delay=0):
    '''
    DESCRIPTION: CLEARS THE CONSOLE AFTER SOME DELAY (IF GIVEN)
    INPUT: DELAY (OPTIONAL)
    OUTPUT: NONE
    '''
    if delay != 0:
        sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def t_print(s, color=d_color, end=''):
    '''
    DESCRIPTION: TYPEWRITER EFFECT
    INPUT: STRING
    OUTPUT: PRINTS EACH CHARACTER ONE BY ONE AFTER A DELAY OF 0.04s FOR EACH
    '''
    for char in s:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        sleep (0.04)
    if end:
        sys.stdout.write(end)
    else:
        pass

def t_input(s, color=d_color):
    t_print(s, color)
    return input(colored("\n=>", color))

def draw_board(board_pos):
    clear()
    print("+-----------+")
    print(f"| {board_pos[6]} | {board_pos[7]} | {board_pos[8]} |")
    print("|---|---|---|")
    print(f"| {board_pos[3]} | {board_pos[4]} | {board_pos[5]} |")
    print("|---|---|---|")
    print(f"| {board_pos[0]} | {board_pos[1]} | {board_pos[2]} |")
    print("+-----------+")

def check_win(b, marker):
    return (
    (b[6] == marker and b[7] == marker and b[8] == marker) or
    (b[3] == marker and b[4] == marker and b[5] == marker) or
    (b[0] == marker and b[1] == marker and b[2] == marker) or
    (b[6] == marker and b[3] == marker and b[0] == marker) or
    (b[7] == marker and b[4] == marker and b[1] == marker) or
    (b[8] == marker and b[5] == marker and b[2] == marker) or
    (b[6] == marker and b[4] == marker and b[2] == marker) or
    (b[8] == marker and b[4] == marker and b[0] == marker)
    )

def place_marker(pos, marker, board):
    board[pos - 1] = marker
    return board

def start_turn(name, turn, marker, n_one, m_one, n_two, m_two):
    global used_pos, board_pos
    while True:
        sleep(0.5)
        draw_board(board_pos)
        try:
            pos = int(t_input(f"{name}, PLACE YOUR MARKER (1-9 ON YOUR NUMPAD)"))
        except ValueError:
            t_print("DON'T LEAVE THIS EMPTY BRUH..", "red")
            continue
        if pos in used_pos:
            t_print("POSITION ALREADY TAKEN!", "red")
        elif pos > 9 or pos < 1:
            t_print("ENTER A NUMBER FROM 1 TO 9!", "red")
        else:
            used_pos.append(pos)
            board_pos = place_marker(pos, marker, board_pos)
            win = check_win(board_pos, marker)
            if len(used_pos) == 9 and not win:
                t_print("IT'S A DRAW MY GUY!")
                draw_board(board_pos)
                break
            elif win:
                t_print(f"{name} WINS!")
                draw_board(board_pos)
                break
            else:
                t_print("PLACING MARKER...")
            return not turn
    sleep(1)
    while True:
        restart_q = t_input("DO YOU WANT TO PLAY AGAIN? (Y/N)").lower()
        if restart_q == 'y':
            board_pos = list(' '*9)
            used_pos = []
            play(n_one, m_one, n_two, m_two)
            break
        elif restart_q == 'n':
            t_print('THANKS FOR PLAYING BRUH...')
            sleep(1)
            exit()
        else:
            t_print("Y/N PLEASE...")

def play(n_one, m_one, n_two, m_two):
    one_turn = True
    while True:
        if one_turn:
            one_turn = start_turn(n_one, one_turn, m_one, n_one, m_one, n_two, m_two)
        else:
            one_turn = start_turn(n_two, one_turn, m_two, n_one, m_one, n_two, m_two)

def start(n_one, n_two):
    t_print(f"HI {n_one} AND {n_two}! {n_one}, CHOOSE FOR O OR X!", end="\n")
    while True:
        marker_q = t_input(f"ENTER 1 FOR 'O' AND 2 FOR 'X'.")
        if not marker_q:
            t_print("IT CANNOT BE EMPTY!", 'red', '\n')
            clear(1)
        elif marker_q == '1':
            m_one = 'o'
            m_two = 'x'
            t_print(f"OK THEN, {n_one} CHOSE 'O' AND {n_two} CHOSE 'X'!\nNOW LOADING...")
            break
        elif marker_q == '2':
            m_one = 'x'
            m_two = 'o'
            t_print(f"OK THEN, {n_one} CHOSE 'X' AND {n_two} CHOSE 'O'!\nNOW LOADING...")
            break
        else:
            t_print("PLEASE ENTER 1 OR 2!", "red")
            clear(1)
    sleep(2)
    play(n_one, m_one, n_two, m_two)

def intro():
    clear()
    while True:
        n_one = t_input("NAME OF PLAYER ONE:", "green").upper()
        n_two = t_input("NAME OF PLAYER TWO:", "blue").upper()
        if not n_one or not n_two:
            t_print("DON'T YOU HAVE A NAME BRUH?", 'red', '\n')
            clear(1)
        else:
            break
    start(n_one, n_two)

# MAIN FUNCTION
def main():
    intro()

# CALLING MAIN FUNCTION
if __name__ == "__main__":
    main()
############################################################################################
