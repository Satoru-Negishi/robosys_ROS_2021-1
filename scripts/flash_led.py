#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import subprocess

def cb(data):
    num_list = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    for (nl, count) in zip(num_list, range(16)):
        if data.data == nl:
            bin_num = bin(count)
            for n in range(6 - len(bin_num)):
                bin_num = bin_num[:2] + '0' + bin_num[2:]

            rospy.loginfo("dec_num -> bin_num : %s",bin_num)
            for i in reversed(range(len(bin_num))):
                if i> 1:
                    if bin_num[i] == num_list[1]:
                        onoff = (2 * (i - 1)) - 1
                        subprocess.call("echo %d > /dev/myled0"%(onoff), shell=True)       
                    else:
                        onoff = (2 * (i - 1)) - 2
                        subprocess.call("echo %d > /dev/myled0"%(onoff), shell=True)

def listener():
    rospy.init_node('flash')
    sub = rospy.Subscriber('input', String, cb)
    rospy.spin()

if __name__ == '__main__':
    listener()
