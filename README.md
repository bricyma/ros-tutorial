# ros-tutorial
get_param.py, set_param.py in tutorials
## ros param
- ```global_name = rospy.get_param("/global_name")```, absolute path
- ```relative_name = rospy.get_param("relative_name")```
- ```private_param = rospy.get_param('~private_name')```  only works in the same file
### example
- ```rospy.set_param('/global_name', 'aaa')```
- ```global_name = rospy.get_param("/global_name")``` 

