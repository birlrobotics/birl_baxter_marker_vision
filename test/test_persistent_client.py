#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client():
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts,persistent=True)
        num = AddTwoIntsRequest()
        num.a = 2
        for i in range (100):
            num.b = 2
            if i == 10:
                num.b = 1234
            else:
                num.b = 2                 
            resp1 = add_two_ints(num.a, num.b)
            print(resp1)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    add_two_ints_client()