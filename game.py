
board_list = []
player = "x"
computer = "o"


def sample_board():
    print(""" 
        player - x
        computer - o
                0  |  1  |  2
                -------------- 
                3  |  4  |  5
                --------------
                6  |  7  |  8   
        """)


def new_board():
    for i in range(0,9):
        board_list.append(" ")


def game_board(board_list):
    print(f'  {board_list[0]} | {board_list[1]} | {board_list[2]}')
    print(f'  ----------')
    print(f'  {board_list[3]} | {board_list[4]} | {board_list[5]}')
    print(f'  ----------')
    print(f'  {board_list[6]} | {board_list[7]} | {board_list[8]}')
    print(f'================\n')


def who_start():
    response = None
    while response not in ("y", "n"):
        response = input("Do you want to start? y/n")
    if response == "y":
        return player
    else:
        return computer


def correct_plays(board_list):
    correct_plays_list = []
    for i in range(0,9):
        if board_list[i] == " ":
            correct_plays_list.append(i)
    return correct_plays_list


def win(board_list):
    win_tuple = ((0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 3, 6),
                 (1, 4, 7),
                 (2, 5, 8),
                 (0, 4, 8),
                 (2, 4, 6))
    for i in win_tuple:
        if board_list[i[0]] == board_list[i[1]] == board_list[i[2]] != " ":
            winner = board_list[i[0]]
            return winner
    if " " not in board_list:
        draw = "draw"
        return draw
    return None


def player_move(board_list):
    correct = correct_plays(board_list)
    move = None
    while move not in correct:
        move = int(input("which field do you choose?"))
        if move not in correct:
            print("Field not available - choose another one!")
    return move


def computer_move(board_list, player, computer):
    board_list = board_list[:]
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for move in correct_plays(board_list):
        board_list[move] = computer
        if win(board_list) == computer:
            return move
        board_list[move] = " "
    for move in correct_plays(board_list):
        board_list[move] = player
        if win(board_list) == player:
            return move
        board_list[move] = " "
    for move in best_moves:
        if move in correct_plays(board_list):
            return move


def next_move(move):
    if move == player:
        return computer
    else:
        return player


def congratulations(winner, player, computer):
    if winner != "draw":
        print(winner, 'wins!')
    else:
        print("Draw!")


def main():
    sample_board()
    turn = who_start()
    new_board()
    game_board(board_list)

    while not win(board_list):

        if turn == player:
            move = player_move(board_list)
            board_list[move] = player
        else:
            move = computer_move(board_list, player, computer)
            board_list[move] = computer
        sample_board()
        game_board(board_list)
        turn = next_move(turn)
    winner = win(board_list)
    congratulations(winner, player, computer)

main()

