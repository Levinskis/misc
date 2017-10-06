#!/bin/bash

source /opt/ros/kinetic/setup.bash
roscore > /dev/tty1 & 
sleep 1
rosrun rviz rviz > /dev/tty1 &
source /home/sdc/catkin_ws/devel/setup.sh
rosrun car_udp_server udp_server > /dev/tty2 &
./fake_keyboard.py > /dev/tty2 &
cd /home/sdc/Research/edicar-lidar-pcd-sender; ./edicar_lidar_pcd_sender > /dev/tty3 &
cd /home/sdc/Research/edi-stereo-vision/stereo-vision; ./Test_Bumblebee_inside > /dev/tty4 &

