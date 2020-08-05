#!/usr/bin/env python
import rospy
import sys
import rospkg
sys.path.insert(1,rospkg.RosPack().get_path("udm_arduino_control")+"/source")
from hello_firmata import control_arduino
from udm_arduino_control.srv import udm_arduino, udm_arduinoResponse
import time 

class service_server:
	def __init__(self):
		rospy.init_node("arduino_control")
		self.ard=control_arduino("/dev/ttyUSB0")
		rospy.Service("arduino_custom_server",udm_arduino,self.handle_service)
		rospy.loginfo("arduino service launched")
		self.delay=0
		while not rospy.is_shutdown():
			self.ard.setLed(1)
			time.sleep(self.delay)
			self.ard.setLed(0)
			time.sleep(self.delay)
		
	def handle_service(self, req):
		rep=udm_arduinoResponse()
		try:
			self.delay=req.delay.data
			rep.res=True

		except Exception as e:
			rep.res=False
			print e
		return rep

if __name__ == '__main__':
	service_server()