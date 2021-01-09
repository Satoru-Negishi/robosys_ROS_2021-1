#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node('input')
pub = rospy.Publisher('input', String, queue_size=1)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    str = input("input number[0 - 15]:")
    rospy.loginfo(str)
    pub.publish(str)
    rate.sleep()


