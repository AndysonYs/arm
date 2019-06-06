cd directory
catkin_make
source devel/setup.bash
roslaunch arm_gazebo empty_world.launch
roslaunch arm_control rviz.launch
roslaunch arm_control moveit.launch
