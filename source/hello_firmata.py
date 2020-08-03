from pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyUSB0')
board.digital[13].write(1)
it = util.Iterator(board)
it.start()
time.sleep(2)
while True:
    board.digital[13].write(1)
    time.sleep(0.2)
    board.digital[13].write(0)
    time.sleep(0.2)