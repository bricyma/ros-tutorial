import rospy

if __name__ == "__main__":
    rospy.init_node("set_param", anonymous=True)
    rospy.set_param('/global_name', 'aaaaa')
    rospy.spin()
