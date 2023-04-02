import pyfirmata
import time


class MotorCtrl:
    def __init__(self, board_port, dir_pin, logic_pin):
        self.dir_pin = dir_pin
        self.logic_pin = logic_pin
        self.board = pyfirmata.Arduino(board_port) # '/dev/ttyACM0'
        self.board.digital[dir_pin].mode = pyfirmata.OUTPUT
        self.board.digital[logic_pin].mode = pyfirmata.OUTPUT
        self.sleep_tm = 0.001
    
    def moveDist(self, dist, dir):
        self.board.digital[self.dir_pin].write(dir)
        for x in range(int(dist)):
            tg = self.sleep_tm + (self.sleep_tm - (((dist - x) / dist) * self.sleep_tm))
            self.board.digital[self.logic_pin].write(1)
            time.sleep(tg)
            self.board.digital[self.logic_pin].write(0)

        # break sudo chmod a+rw /dev/ttyACM0
        time.sleep(0.5)
            
    # //  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
    # //  // Makes 200 pulses for making one full cycle rotation
    # //  for(int x = 0; x < 800; x++) {
    # //  digitalWrite(stepPin,HIGH); 
    # //  delayMicroseconds(500); 
    # //  digitalWrite(stepPin,LOW); 
    # //  delayMicroseconds(500); 
    # //  }
    # //  delay(1000); // One second delay


if __name__ == '__main__':    
    mtr_ctrl = MotorCtrl('/dev/ttyACM0', 5, 2)
    mtr_ctrl.moveDist(1000,0)