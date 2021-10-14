import InputOutputClass
import Constants


def main():
    board_list: list[int] = []
    who_is_play = Constants.X

    #reset game
    for i in range(9):
        board_list.append(Constants.Empty)

    while not isGameOver(board_list):

        InputOutputClass.InputOutputClass.printBoard(board_list)
        user_choice = InputOutputClass.InputOutputClass.getUserChoice(board_list, who_is_play)
        board_list[user_choice - 1] = who_is_play
        who_is_play = Constants.O / who_is_play

    InputOutputClass.InputOutputClass.printBoard(board_list)
    print("Game Over!!!")


def isGameOver(board_list: list[int]) -> bool:
    tie = True
    for square in board_list:
        if square == Constants.Empty:
            tie = False
    return tie

if __name__ == '__main__':
    main()
