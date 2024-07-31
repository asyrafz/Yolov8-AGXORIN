### Set up the workspace

1. Open the Terminal and create a workspace and move to the folder
   
###

    mkdir -p ~/ros2_ws/src
   
###

    cd ~/ros2_ws/src/
    

![Alt text](https://github.com/user-attachments/assets/543276aa-ba9a-487d-b50b-103bd1a05652)

2. Add the ROS tutorials to the workspace
   
###

      git clone https://github.com/ros/ros_tutorials.git -b foxy-devel
   
###

3. Add the package dependencies
   
###

      cd ~/ros2_ws/
      
      rosdep install -i --from-path src --rosdistro foxy -y
   
###
   
###



   
###



