### Set up the workspace

Step 1-7 refering to [E-Consystems.com](https://www.e-consystems.com/blog/camera/products/all-you-need-to-know-about-how-to-install-ros2-on-jetson-orin-using-nilecam81/?srsltid=AfmBOoppc5dbTDD7Q748CfQvNCjXBgAuqpdomlP48yyHNatd9u0OIOHG)

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

![rosdep-install-i-from-path-src-rosdistro-foxy-y](https://github.com/user-attachments/assets/27678c97-97d6-4500-a866-dbe65fcd794e)

###

4. Colcon Build – Build your workspace
  
###

      sudo apt update
      
      sudo apt install python3-colcon-common-extensions
      
      colcon build

###

![colcon-build](https://github.com/user-attachments/assets/05779c41-ac2e-4f78-a5c9-106a4fdcafe0)
 
###

5. Source the created workspace in Bash file

###

      sudo apt-get install gedit
      gedit ~/.bashrc

###

Add the following line to the bottom of bashrc file

###

      source ~/ros2/install/setup.bash

###

6. Create a Package
   Open a new terminal

###

      cd ~/ros2_ws/src

###

Now, let’s create a package named cv_basics.

###

      ros2 pkg create --build-type ament_python cv_basics --dependencies rclpy image_transport cv_bridge sensor_msgs std_msgs opencv2

###

7. Then, Create the Python script for Publisher and Subscriber






