#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def listener():
    rospy.init_node('get_param', anonymous=True)
    # private name
    # rospy.set_param('~global_name', 'aaffaaa')
    private_name = rospy.get_param("~private_name")
    global_name = rospy.get_param("/global_name")
    print global_name
    print 'private name: ', private_name


if __name__ == '__main__':
    listener()
    rospy.spin()
