import numpy as np
import pyfirmata
import time

class MoveTranslator:
    def  __init__(self, board_width: float, board_length: float) -> None:
        self.board_width    = board_width
        self.board_length   = board_length
    

    def calibratePos(self):
        self.board_width    = self.getWidth()
        self.board_length   = self.getLength()


