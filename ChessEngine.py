"""
File reponsible for determining the valid moves of the match and
displaying the current state of the game
"""

class GameState():
    def __init__(self):
        #8x8 2d list, each element of list has 2 characters.
        #First char represents the color while the second represents the type
        #"--" represents empty space 
        self.board = [

            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]

        ]       #numpy array is potentially more efficient

