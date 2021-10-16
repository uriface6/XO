import InputOutputClass
import Constants
from typing import List

def main():
    board_list: list[int] = []
    who_is_play = Constants.X
    counter = 0
    #win = Constants.Empty

    #reset game
    for i in range(9):
        board_list.append(Constants.Empty)

    while not isGameOver(board_list):

        InputOutputClass.InputOutputClass.printBoard(board_list)
        user_choice = InputOutputClass.InputOutputClass.getUserChoice(board_list, who_is_play)
        board_list[user_choice - 1] = who_is_play
        who_is_play = Constants.O / who_is_play
        if counter >= 4:
            win = InputOutputClass.InputOutputClass.winCheck(board_list)
            if win == Constants.X:
                InputOutputClass.InputOutputClass.printBoard(board_list)
                print("XXXXXXXXXXXXXXXXXX")
                print("X is the winner!!!")
                print("XXXXXXXXXXXXXXXXXX")
                break
            elif win == Constants.O:
                InputOutputClass.InputOutputClass.printBoard(board_list)
                print("OOOOOOOOOOOOOOOOOO")
                print("O is the winner!!!")
                print("OOOOOOOOOOOOOOOOOO")
                break
        counter += 1

    if isGameOver(board_list) and win == Constants.Empty:
        InputOutputClass.InputOutputClass.printBoard(board_list)
        print("Game Over - Tie!!!")




def isGameOver(board_list: List[int]):
    tie = True
    for square in board_list:
        if square == Constants.Empty:
            tie = False
    return tie

if __name__ == '__main__':
    main()
