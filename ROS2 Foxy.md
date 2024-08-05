## How to install ROS2 on AGX Orin

<p align="center" width="100%">
    <img width="33%" src="https://images.squarespace-cdn.com/content/v1/606d378755a86f589aa297b7/1620754015606-3M9GLQWXM2CMTLKQAZ70/103c1-d6fd5322bd2ddc06530d8352fcab20f0bca08c06_2_420x500.png"> 
</p>

### System Setup

### Set Locale

        locale  # check for UTF-8

        sudo apt update && sudo apt install locales
        sudo locale-gen en_US en_US.UTF-8
        sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
        export LANG=en_US.UTF-8
        
        locale  # verify settings

### Add the ROS 2 apt repository

You will need to add the ROS 2 apt repository to your system.
First ensure that the Ubuntu Universe repository is enabled.

        sudo apt install software-properties-common
        sudo add-apt-repository universe

Now add the ROS 2 GPG key with apt.

    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

Then add the repository to your sources list.

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

### Install development tools and ROS tools

        sudo apt update && sudo apt install -y \
          libbullet-dev \
          python3-pip \
          python3-pytest-cov \
          ros-dev-tools
        
        # install some pip packages needed for testing
        python3 -m pip install -U \
          argcomplete \
          flake8-blind-except \
          flake8-builtins \
          flake8-class-newline \
          flake8-comprehensions \
          flake8-deprecated \
          flake8-docstrings \
          flake8-import-order \
          flake8-quotes \
          pytest-repeat \
          pytest-rerunfailures \
          pytest
        # install Fast-RTPS dependencies
        sudo apt install --no-install-recommends -y \
          libasio-dev \
          libtinyxml2-dev
        # install Cyclone DDS dependencies
        sudo apt install --no-install-recommends -y \
          libcunit1-dev

### Get ROS 2 code
        
        mkdir -p ~/ros2_foxy/src
        cd ~/ros2_foxy
        vcs import --input https://raw.githubusercontent.com/ros2/ros2/foxy/ros2.repos src

### Install dependencies using rosdep

        sudo apt upgrade        

in :~/ros2_foxy

        sudo rosdep init
        rosdep update  <<<<<<<< JA01 berhenti sini <<<<
        export ROS_DISTRO=foxy
        export ROS_PYTHON_VERSION=3
        rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-5.3.1 urdfdom_headers"

OR if error

        sudo apt-get install ros-foxy-fastrtps
        sudo rosdep init
        rosdep update
        sudo apt-get install ros-foxy-desktop

## Test "fastrtps" installed properly

        dpkg -l | grep fastrtps
        python3 -c "import pyfastdds"

make example.py  <<<<<<update>>>> abaikan dulu sebab nak fokus rosbridge

        import pyfastdds
        # Create a DomainParticipant
        participant = pyfastdds.DomainParticipant(0)
        # Create a Topic
        topic = participant.create_topic("example_topic", "example_type")
        print("Topic created:", topic.get_name())

### run example.py

        python3 example.py

## Install ROS Bridge

Clone the ROS Bridge repository:

        cd ~/ros2_foxy/src
        git clone https://github.com/RobotWebTools/rosbridge_suite.git

Build the workspace:

        cd ~/ros2_foxy
        colcon build --packages-select rosbridge_suite

If the script runs successfully, it means that the fastrtps library is working properly. 

    ros2 pkg list | grep fastrtps
    ros2 run demo_nodes_py talker
    sudo apt-get install ros-foxy-pyfastdds
    
----

### Run ROS Bridge

Start a ROS2 node:

        ros2 run rosbridge_server rosbridge_websocket

### Verify Installation

Check if the ROS Bridge server is running:

        ros2 node list
You should see a node named rosbridge_websocket.
Use a WebSocket client (like a web browser with a WebSocket extension) to connect to ws://localhost:9090 (default port).







