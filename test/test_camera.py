#!/usr/bin/env python
import tf
import numpy as np
import rospy
from geometry_msgs.msg import Pose
import ipdb
from birl_baxter_vision.srv import *

req = get_poseRequest()
req.flag.data = True
add_two_ints = rospy.ServiceProxy('get_pose_from_base_camera', get_pose)
resp1 = add_two_ints(req)
print resp1