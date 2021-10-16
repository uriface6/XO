import Constants
from typing import List


class InputOutputClass:

    def __init__(self):
        pass

    @staticmethod
    def getUserChoice(board_list: List[int], who_is_play: int) -> int:
        player_choice_int: int = 0
        player_choice_str: str = ""

        while not InputOutputClass.isTurnValid(board_list, player_choice_int):

            if who_is_play == Constants.O:
                print("It's O turn")
            elif who_is_play == Constants.X:
                print("It's X turn")

            player_choice_str = input("Enter your choice (number between 1 - 9, empty square): ")
            try:
                player_choice_int = int(player_choice_str)
            except ValueError:
                # Handle the exception
                pass

        return player_choice_int

    @staticmethod
    def isTurnValid(board_list: List[int], player_choice: int) -> bool:
        is_turn_valid = False
        if 0 < player_choice < 10 and board_list[player_choice - 1] == Constants.Empty:
            is_turn_valid = True
        return is_turn_valid

    @staticmethod
    def printBoard(board_list: List[int]):
        square_index = 0
        for i in range(3):
            print("|", end="")
            for j in range(3):
                InputOutputClass.printSquare(board_list[square_index], square_index + 1)
                print("|", end="")
                square_index += 1
            print("")

    @staticmethod
    def printSquare(square: int, square_index: int):
        if square == Constants.X:
            print("X", end="")
        elif square == Constants.O:
            print("O", end="")
        elif square == Constants.Empty:
            print(square_index, end="")

    @staticmethod
    def winSpecificCheck(board_list: List[int], start_square: int, square_jump_row: int, square_jump_col: int) -> int:
        testing_shape = board_list[start_square]
        counter = 0
        isWin = True
        curr_square = start_square + square_jump_row

        while curr_square < 9:
            # for curr_square in range(start_square, 3, square_jump_row):
            if testing_shape != board_list[curr_square] or testing_shape == Constants.Empty:
                isWin = False
            counter += 1
            if counter >= 2:
                counter = 0
                if isWin:
                    break
                curr_square += square_jump_col
                if curr_square >= 8 or curr_square - square_jump_col >= 8:
                    break
                else:
                    isWin = True
                testing_shape = board_list[curr_square]
            curr_square += square_jump_row
        if isWin:
            return testing_shape
        else:
            return Constants.Empty

    @staticmethod
    def winCheck(board_list: List[int]) -> int:
        win = InputOutputClass.winSpecificCheck(board_list, 0, 1, 1)
        if win != Constants.Empty:
            return win
        win = InputOutputClass.winSpecificCheck(board_list, 0, 3, -5)
        if win != Constants.Empty:
            return win
        win = InputOutputClass.winSpecificCheck(board_list, 0, 4, 1)
        if win != Constants.Empty:
            return win
        win = InputOutputClass.winSpecificCheck(board_list, 2, 2, 4)
        return win
