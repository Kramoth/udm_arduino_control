#!/usr/bin/env python

import sys
import rospy
from udm_arduino_control.srv import *
from std_msgs.msg import Float32
def client(delay):
    rospy.wait_for_service('arduino_custom_server',)
    try:
        blink = rospy.ServiceProxy("arduino_custom_server", udm_arduino)
        rep = blink(delay)
        return rep
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "usage %s 0.5 for example"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            delay=Float32()
            delay.data=float(sys.argv[1])
            client(delay)
        except Exception as e:
            print e
            sys.exit(1)
    else:
        print(usage())
        sys.exit(1)
