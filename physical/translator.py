import numpy as np
import pyfirmata
import time

class MoveTranslator:
    """Class for tranlating chess positional moves to actual motor movement"""

    def  __init__(self, board_width: float) -> None:
        self.board_width    = board_width
    

    def calibratePos(self):
        """ Run calibration routine to get board physical dims """
        self.board_width    = self.getWidth()
        self.square_dim     = self.board_width /8.0 # Chessboard has 8x8 struct

    def str2pos(self, pos: str):
        """ Convert positon string to machine understandable integer x,y coords """
        if pos is not None:
            char_val    = ord(pos[0]) - ord('a') # Getting charater int relative to letter 'a'
            num_val     = int(pos[1])

            if char_val > 7 or char_val < 0 or num_val < 1 or num_val > 8:
                return None

            x_coord     = (char_val + 1) * self.square_dim # +1 to 1 index the val
            y_coord     = (num_val) * self.square_dim

            return x_coord, y_coord
        
        else:

            return None
    def get2FroCoords(self, pos_pair: str):
        """ Gets x,y coords for source and target piece positions """
        if(pos_pair is not None and len(pos_pair) == 4):
            src_x, src_y = self.str2pos(pos_pair[0:2])
            tgt_x, tgt_y = self.str2pos(pos_pair[2:4])
            
            if(src_x is None or src_y is None or
                tgt_x is None or tgt_y is None):
                return None
            else:
                return src_x, src_y, tgt_x, tgt_y
        else:        
            return None
