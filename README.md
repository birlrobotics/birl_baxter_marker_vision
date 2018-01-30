# Pick and Place demo
Go to baxter_ws
`$ ./baxter.sh`
## Camera setup
###  Dependencies
Install openni2
### Tutorial
Checking xtion's ｓｔａｔｅ
`$ lsusb`
If xtion has not the ability of writing, you need add it by yourself, Go to `usb` direction 
`$ cd /dev/bus/usb/001`
Add xtion's write mode 
`/dev/bus/usb/001$ sudo chmod 666 007`
Open xtion
`$ roslaunch openni2_launch openni2.launch`
You should get similar information like below

    [ INFO] [1517284499.269441293]: Initializing nodelet with 4 worker threads.
    [ INFO] [1517284502.066124112]: Device "1d27/0601@1/7" found.
    Warning: USB events thread - failed to set priority. This might cause loss of data...
    [ INFO] [1517284505.936259130]: Starting color stream.
    [ INFO] [1517284506.338848684]: using default calibration URL
    [ INFO] [1517284506.338940936]: camera calibration URL: file:///home/tony/.ros/camera_info/rgb_PS1080_PrimeSense.yaml
Check whecther launch xtion correctly
1. `rosrun rviz rviz `
2. click `Add-->Image`
3. Switch Image topic to `/camera/rgb/image_raw`

You should be able to see image in a  window

Otherwise you may not open it successfully. you can restart it again after checking that you have right configuration.

## URDF setup
###  Dependencies
https://github.com/birlrobotics/birl_baxter_online_urdf_update

### Tutorial
I am thinking to make it become a launch file, but because time need to be update every time when updating urdf, so right now just keep it as before

 Get your computer's current time with this bash command
` $ date +'secs:%s   nsecs:%N'`

 Publish the URDFConfiguration message to the /robot/urdf topic. From a baxter.sh shell: 
 `$ rostopic pub -l /robot/urdf baxter_core_msgs/URDFConfiguration -f ***.yaml`
Now, to view our masterpiece in RViz: 

`$ rosrun rviz rviz`

## Aruco marker setup
###  Dependencies
https://github.com/pal-robotics/aruco_ros

### Tutorial
Open aruco
`$ roslaunch birl_baxter_vision aruco_setup.launch`

Publish relation betwen `base` and `camera_link` and relation `aruco_marker_582` and `aruco_marker_582_pick`  When doing this, you need put a marker in front of camera to let it capture `aruco_marker_582`  otherwise `aruco_marker_582_pick`  cannot  be got

`$ roslaunch birl_baxter_vision baxter_base_camera.launch`

##  Trac_ik setup
###  Dependencies
https://github.com/baxter-flowers/trac_ik_baxter
### Tutorial
Open trac_ik service
`$ roslaunch trac_ik_baxter ik_server.launch`

## Demo
###  Dependencies
make sure trac_ik service has been running
`$ rosrun birl_baxter_motion_generation grab_object_base_camera_trac_ik.py`
