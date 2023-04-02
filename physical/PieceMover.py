from MotorCtrl import MotorCtrl
from Translator import MoveTranslator


class PieceMover():
    def __init__(self, board_width: float) -> None:
        self.translator = MoveTranslator(board_width)
        self.x_ctrl = MotorCtrl('/dev/ttyACM0', 5, 2)
        self.y_ctrl = MotorCtrl('/dev/ttyACM0', 6, 3)
        self.curr_x = None
        self.curr_y = None
    
    def moveA2B(self, ab_pos:str):
        if(self.curr_x is not None and self.curr_y is not None):
            
            # Src pos and Tgt pos 
            a_x, a_y, b_x, b_y = self.translator.get2FroCoords(ab_pos)
            print(f"curr coords: {self.curr_x, self.curr_y}")
            print(f"src coords: {a_x, a_y}, tgt coords: {b_x, b_y}")

            # Get to base cross
            print(f"move neg base cross: {self.translator.square_dim, self.translator.square_dim}")
            self.x_ctrl.moveDist(self.translator.square_dim, 0)
            self.y_ctrl.moveDist(self.translator.square_dim, 0)
        
            # Get to src cross
            if(self.curr_x > a_x):
                print(f"move neg x: {self.curr_x - a_x}")
                self.x_ctrl.moveDist(self.curr_x - a_x, 0)
            else:
                print(f"move pos x: {a_x - self.curr_x}")
                self.x_ctrl.moveDist(a_x - self.curr_x, 1)
                
            if(self.curr_y > a_y):
                print(f"move neg y: {self.curr_y - a_y}")
                self.y_ctrl.moveDist(self.curr_y - a_y, 0)
            else:
                print(f"move pos y: {a_y - self.curr_y}")
                self.y_ctrl.moveDist(a_y - self.curr_y, 1)    
            
            # Get to middle
            print(f"move pos base cross: {self.translator.square_dim, self.translator.square_dim}")
            self.y_ctrl.moveDist(self.translator.square_dim, 1)
            self.x_ctrl.moveDist(self.translator.square_dim, 1)
            
            # Pick the piece
            print(f"Pick piece")
            # TODO
            
            # Get to src cross
            print(f"move neg base cross: {self.translator.square_dim, self.translator.square_dim}")
            self.x_ctrl.moveDist(self.translator.square_dim, 0)
            self.y_ctrl.moveDist(self.translator.square_dim, 0)
                                 
            # Set new curr pos                                 
            self.curr_x, self.curr_y = a_x, a_y
            
            # Get to tgt cross
            if(self.curr_x > b_x):
                print(f"move neg x: {self.curr_x - b_x}")
                self.x_ctrl.moveDist(self.curr_x - b_x, 0)
            else:
                print(f"move pos x: {b_x - self.curr_x}")
                self.x_ctrl.moveDist(b_x - self.curr_x, 1)
                
            if(self.curr_y > b_y):
                print(f"move neg y: {self.curr_y - b_y}")
                self.y_ctrl.moveDist(self.curr_y - b_y, 0)
            else:
                print(f"move pos y: {b_y - self.curr_y}")
                self.y_ctrl.moveDist(b_y - self.curr_y, 1)    
            
            # Get to middle
            print(f"move pos base cross: {self.translator.square_dim, self.translator.square_dim}")
            self.y_ctrl.moveDist(self.translator.square_dim, 1)
            self.x_ctrl.moveDist(self.translator.square_dim, 1)
            
            # Drop the piece
            # TODO
            
            # Set new curr pos                                 
            self.curr_x, self.curr_y = b_x, b_y
                
            return
            
if __name__ == '__main__':
    mvr = PieceMover(1000)
    mvr.curr_x = 0.0
    mvr.curr_y = 0.0
    mvr.moveA2B('a1a6')