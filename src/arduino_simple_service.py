#!/usr/bin/env python
import rospy
import sys
import rospkg
sys.path.insert(1,rospkg.RosPack().get_path("udm_arduino_control")+"/source")
from hello_firmata import control_arduino
from std_srvs.srv import SetBool, SetBoolResponse

class service_server:
	def __init__(self):
		rospy.init_node("arduino_control")
		self.ard=control_arduino("/dev/ttyUSB0")
		rospy.Service("arduino_simple_server",SetBool,self.handle_service)
		rospy.loginfo("arduino service launched")
		rospy.spin()
		
	def handle_service(self, req):
		rep=SetBoolResponse()
		try:
			self.ard.setLed(req.data)
			rep.success=True
			rep.message="succeed"

		except Exception as e:
			rep=SetBoolResponse()
			rep.success=False
			rep.message=e
		return rep

if __name__ == '__main__':
	service_server()