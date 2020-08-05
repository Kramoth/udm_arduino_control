import sys
from pyfirmata import Arduino, util
import time




class control_arduino:
	def __init__(self,port):
		print(port)
		self.board=Arduino(port)
		self.it=util.Iterator(self.board)
		self.it.start()
		time.sleep(2)
		print("ok")

	def blink(self):
		while True:
			self.board.digital[13].write(1)
			time.sleep(2)
			self.board.digital[13].write(0)
			time.sleep(2)

	def setLed(self, data):
		self.board.digital[13].write(data)

if __name__ == '__main__':
	if len(sys.argv)>1:
		try:
			ard=control_arduino(sys.argv[1])
			ard.blink()
		except Exception as e:
			print(e)
			sys.exit(1)
	else:
		try:
			control_arduino("/dev/ttyACM0")
			ard.blink()
		except Exception as e:
			print(e)
			sys.exit(1)
