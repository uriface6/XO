import Constants


class InputOutputClass:

    def __init__(self):
        pass

    @staticmethod
    def getUserChoice(board_list: list[int], who_is_play: int) -> int:
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
    def isTurnValid(board_list: list[int], player_choice: int) -> bool:
        is_turn_valid = False
        if 0 < player_choice < 10 and board_list[player_choice - 1] == Constants.Empty:
            is_turn_valid = True
        return is_turn_valid

    @staticmethod
    def printBoard(board_list: list[int]):
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
