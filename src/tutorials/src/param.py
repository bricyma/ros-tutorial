#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from dynamic_reconfigure.server import Server
from tutorials.cfg import gpsConfigConfig


class testParam:
    def __init__(self):
        self.offset = rospy.get_param('yaw_angle_offset', 0)
        self.srv = Server(gpsConfigConfig, self.reconfigure)

    def reconfigure(self, config, level):
        if config.enable_calibrate:
	    self.offset = config.yaw_offset
        print 'offset: ', self.offset
        return config


if __name__ == "__main__":
    print 'start param test'
    rospy.init_node('esr_interface', anonymous=False)
    _ = testParam()
    rospy.spin()
