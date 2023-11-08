import mint
import colorama
colorama.init(autoreset=True)

def check_pos(User_input):
    try:
        int(User_input)
    except:
        return False
    does_contain = False
    for _ in table:
        if mint.in_out.list_contain(_, int(User_input)):
            does_contain = True
    return does_contain


def pr_table():
    for b in table:
        temp_pr = ""
        for B in b:
            if len(str(B)) == 1:
                if (str(B) != "X") and (str(B) != "O"):
                    temp_pr += colorama.Fore.WHITE + str(B)+"   "
                else:
                    temp_pr += colorama.Fore.RED + str(B)+"   "
            else:
                temp_pr += colorama.Fore.WHITE + str(B) + "  "
        print("\n", temp_pr)


def game_check():
    win = None
    # the following code checks all winning possibilities to look for a winner
    for t in ["X", "O"]:
        # the following piece of code checks the rows for a winner
        for l in table:
            temp_last_seen = 0
            for L in l:
                if L == t:
                    temp_last_seen += 1
                    if temp_last_seen >= win_cond:
                        win = t
                else:
                    temp_last_seen = 0
        # the following piece of code checks the columns for a winner
        for l in range(scale):
            temp_last_seen = 0
            for L in table:
                if L[l] == t:
                    temp_last_seen += 1
                    if temp_last_seen >= win_cond:
                        win = t
                else:
                    temp_last_seen = 0
        # the following code checks for diagonal winning cases
        for l in range(scale):
            for L in range(scale):
                if table[l][L] == t:
                    temp_all_true = True
                    for v in range(win_cond):
                        try:
                            if not (table[l+v][L+v] == t):
                                temp_all_true = False
                        except:
                            temp_all_true = False
                            break
                    if temp_all_true:
                        win = t
                    temp_all_true = True
                    for v in range(win_cond):
                        try:
                            if not (table[l - v][L + v] == t):
                                temp_all_true = False
                        except:
                            temp_all_true = False
                            break
                    if temp_all_true:
                        win = t

    # the following code checks whether to announce a draw or not and also returns the functions work
    if win is None:
        table_full = True
        for p in table:
            for pp in p:
                if (not (pp == "X")) and (not (pp == "O")):
                    table_full = False
        if table_full:
            return "draw"
    else:
        return win


# this piece prepares the game conditions such as the scale.
scale = ""
win_cond = 0
fine = False
while not fine:
    scale = input(colorama.Fore.YELLOW +"\nenter the scale of the game. min 3 max 10 (example: write 6 for a 6*6 game) ")
    try:
        scale = int(scale)
        if 3 <= scale <= 10:
            fine = True
        else:
            continue
    except:
        continue
    if scale < 5:
        win_cond = 3
    elif scale >= 5:
        win_cond = 4
    print(colorama.Fore.YELLOW +"you have to align", colorama.Fore.RED +str(win_cond),colorama.Fore.YELLOW + "X's or O's in order to win")

# this for loop creates the default table list
table = []
for R in range(scale):
    table.append([])
    for r in range(scale):
        table[-1].append((R * scale) + r + 1)

# executor loop. most of the job is done by functions but this loop just runs them.
turn: str = "X"
while True:
    pr_table()
    pos = -1
    # the following while keeps getting inputs until one is suitable for the game conditions.
    while not check_pos(pos):
        if turn == "X":
            pos = input(colorama.Fore.GREEN +"\nplayer 1: ")
        else:
            pos = input(colorama.Fore.GREEN +"\nplayer 2: ")
    # the following for loop replaces the selected element in the table with either X or O.
    for i in range(len(table)):
        for x in table[i]:
            if x == int(pos):
                table[i][table[i].index(x)] = turn
    # the following ifs check the game condition and see if they should end it.
    if game_check() == "X":
        print(colorama.Fore.BLUE +"the game ends and player 1 wins!!!")
        exit(0)
    elif game_check() == "O":
        print(colorama.Fore.BLUE +"the game ends and player 2 wins!!!")
        exit(0)
    elif game_check() == "draw":
        print(colorama.Fore.BLUE +"the game ends with a draw")
        exit(0)
    # the following if condition switches the turns if the game is still on going.
    if turn == "X":
        turn = "O"
    else:
        turn = "X"