#!/usr/bin/env python
import tf
import numpy as np
import rospy
from geometry_msgs.msg import Pose
from trac_ik_baxter.srv import *
import ipdb

pose_sum = []
listener = None 
   

def cb(req):  
    global listener
    marker_pose = []
    if req.flag is True:
        global pose_sum
        rospy.loginfo("get in aruco_marker_582_pick_frame cb")
        while not rospy.is_shutdown():
            try:
                (trans,rot) = listener.lookupTransform("/base", "/aruco_marker_582_pick_frame", rospy.Time())
                marker_pose_unfilter = Pose()
                marker_pose_unfilter.position.x = trans[0]
                marker_pose_unfilter.position.y = trans[1]
                marker_pose_unfilter.position.z = trans[2] 
                marker_pose_unfilter.orientation.x = rot[0]
                marker_pose_unfilter.orientation.y = rot[1]
                marker_pose_unfilter.orientation.z = rot[2]
                marker_pose_unfilter.orientation.w = rot[3]
                resp = get_poseResponse()
                resp.pose = marker_pose_unfilter
                print("get marker pose", resp.pose)
                return resp
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
                print "Service call failed: %s"%e


def main():
    global listener
    rospy.init_node('get_marker_pose_from_base_camera')
    listener = tf.TransformListener()
    listener.waitForTransform("/base", "/aruco_marker_582_pick_frame", rospy.Time(), rospy.Duration(4.0))
    rospy.Service('get_pose_from_base_camera', get_pose , cb)
    print "get_pose_from_base_camera"
    rospy.spin()

if __name__ == "__main__":
    main()
