
EMPTY = " "
TIE = "TIE"
NUM = 9
USED = []
def ask_number (name1,question):
    response = None
    print("\a")
    print("\n")
    print("NOW")
    print(name1)
    while response not in ("0", "1", "2", "3", "4", "5", "6", "7", "8"):
        response = input(question)
        if response in ("0", "1", "2", "3", "4", "5", "6", "7", "8"):
            response = int(response)
            USED.append(response)
            return response
        else:
            print(name1, ", YOU CHOOSE A INVALID POSITION")
            print("RE-ENTER YOUR POSITION\n")



def new_board():
    board = []
    for square in range(NUM):
        board.append(EMPTY)
    return board
def display_board(board):
    print("\t\tIT'S YOURS BOARD")
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "--|---|--")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "--|---|--")
    print("\t", board[6], "|",  board[7], "|", board[8], "\n")
def instruction():

    print("""
                           _________       _________              _________   ___     _________            _________    __________   __________
                          /___  ____\  /\  |  _____/             /___  ____\ // \\\   |  _____/            /___  ____\  / /______\ \  | |______/
                              /\       ||  | |         _______       /\     //   \\\  | |        _______       /\       | |      | |  | |
                              ||       ||  | |        /_______\      ||    //_____\\\ | |       /_______\      ||       | |      | |  | |______          
                              ||       ||  | |                       ||    ||_____|| | |                      ||       | |      | |  | |_____/ 
                              ||       ||  | |______                 ||    ||     || | |_____                 ||       | |______| |  | |______
                              \/       \/  |_______/                 \/    \/     \/ |______/                 \/       \_________/   |_______/




                              """)
    print("\a")

    print("\t\t\t           <-:: WELCOME TO THE ::->\n")
    print("                                         TIC-TAC-TOE")
    print("                        TIC-TAC-TOE IS A-- NOUGHTS AND CROSSES GAME\n")
    print("\t        you will make your move known by entering a number, 0-8. The number \n"
          "                      will correspond to the board position as illustrated:\n")
    print("""                              
                                     0 | 1 | 2
                                    ---|---|----
                                     3 | 4 | 5
                                    ---|---|----
                                     6 | 7 | 8  
                                            """)
    input("PRESS TO THE ENTER KEY TO START GAME :--")

def winner(board):
    way = ((0, 1, 2),
           (3, 4, 5),
           (6, 7, 8),
           (0, 3, 6),
           (1, 4, 7),
           (2, 5, 8),
           (0, 4, 8),
           (2, 4, 6))
    for row in way:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE


def head(board):
    turn = 0
    name1 = input("ENTER NAME 'PLAYER 1:-'  \n")
    name2 = input("ENTER NAME 'PLAYER 2:-'  \n")
    print("\n")
    print(name1, "YOU WILL GO WITH--'X'")
    print(name2, "YOU WILL GO WITH--'0'")
    print("\n")
    print("\t\tBEST OF LUCK!!!!!")
    for i in range(NUM):
        if turn == 0:
            v = "X"
            player1 = ask_number(name1, "CHOOSE YOUR POSITION BETWEEN(0-8):-  ")
            if board[player1] != EMPTY:
                print(name1, "\nYOU CHOOSE USED POSITION")
                continue

            else:
                board[player1] = v
                display_board(board)
                print("YOURS USED POSITIONS ARE ::-\n", USED)
                win = winner(board)
                if win != TIE:
                    if not win:
                        turn = 1

                    else:
                        print("\a")
                        print("\n")
                        print(name1, "CONGRATS YOU WIN THIS GAME\n")
                        break
                else:
                    print("\a")
                    print("\n")
                    print("TIE\n" + "GAME OVER!!!")
        else:

            x = "0"
            player2 = ask_number(name2, "CHOOSE YOUR POSITION BETWEEN(0-8):-  ")

            if board[player2] != EMPTY:
                print(name2, "\nYOU CHOOSE USED POSITION")
                continue

            else:

                board[player2] = x
                display_board(board)
                print("YOURS USED POSITIONS ARE ::-\n", USED)
                win=winner(board)
                if win != TIE:
                    if not win:
                        turn = 0


                    else:
                        print("\a")
                        print("\n")
                        print(name2, "CONGRATS YOU WIN THIS GAME\n")
                        break
                else:
                    print("\a")
                    print("\n")
                    print("TIE\n" + "GAME OVER!!!")

def main():
    print("\a")
    instruction()
    board = new_board()
    display_board(board)
    head(board)

main()
input("PRESS TO THE ENTER KEY TO EXIT GAME:-- ")







