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












