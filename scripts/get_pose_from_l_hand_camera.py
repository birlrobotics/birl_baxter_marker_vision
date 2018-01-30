#!/usr/bin/env python
import tf
import numpy as np
import rospy
from geometry_msgs.msg import Pose
from trac_ik_baxter.srv import *
import ipdb

pose_sum = []
listener = None 

def ava_fuc(pose_sum):
    x = []
    y = []
    z = []
    w_x = []
    w_y = []
    w_z = []
    w_w = []
    
        
    for idx in pose_sum:
        x.append(idx[0])
        y.append(idx[1])
        z.append(idx[2])
        w_x.append(idx[3])
        w_y.append(idx[4])
        w_z.append(idx[5])
        w_w.append(idx[6])
    marker_pose = Pose()
    a = np.array(x)
    marker_pose.position.x = np.mean(a)
    b = np.array(y)
    marker_pose.position.y  = np.mean(b)
    c = np.array(z)
    marker_pose.position.z  = np.mean(c)
    d = np.array(w_x)
    marker_pose.orientation.x = np.mean(d)
    e = np.array(w_y)
    marker_pose.orientation.y = np.mean(e)
    f = np.array(w_z)
    marker_pose.orientation.z = np.mean(f)
    g = np.array(w_w)
    marker_pose.orientation.w = np.mean(g)
    return marker_pose
    

def cb(req):  
    global listener
    marker_pose = []
    if req.flag is True:
        global pose_sum
        rospy.loginfo("get in aruco_marker_582_pick_frame cb")

        #ipdb.set_trace()
        for i in range (10): 
            try:

                (trans,rot) = listener.lookupTransform("/base", "/aruco_marker_582_pick_frame", rospy.Time())
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
                continue
            marker_pose = [trans[0],trans[1],trans[2],rot[0],rot[1],rot[2],rot[3]]
            pose_sum.append(marker_pose)

        resp = get_poseResponse()
        resp.pose = ava_fuc(pose_sum)
        print("get marker pose from left hand camera", resp.pose)
        return resp

def main():
    global listener
    rospy.init_node('get_marker_pose_from_l_hand_camera')
    listener = tf.TransformListener()
    listener.waitForTransform("/base", "/aruco_marker_582_pick_frame", rospy.Time(), rospy.Duration(4.0))
    rospy.Service('get_pose_from_l_hand_camera', get_pose , cb)
    print "get_pose_from_left_hand_camera."
    rospy.spin()

if __name__ == "__main__":
    main()
