# Yolov8-AGXORIN
Tutorial Setup Yolov8 into Jetson AGX Orin Developer Kit

## JETSON AGX Orin (64GB ram)
- Machine: aarch64 
- 5.10.120-tegra
- Python: 3.8.10
- CUDA: 11.4.315
- cuDNN: 8.6.0.166
- TensorRT: 8.5.2.2
- Jetpack: 5.1.2

## Extra
    sudo apt-get update && sudo apt-get install python-pip python3-pip

    Jtop:
    sudo pip3 install -U jetson-stats

then, reboot

### Path reg
    sudo apt update
    
    sudo apt-get install nano
    
    nano /home/$USER/.bashrc

    export PATH=/usr/local/cuda-11.4/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64:$LD_LIBRARY_PATH
    <add below>
    export PATH=/home/agx_orin/.local/bin:$PATH
    export LD_LIBRARY_PATH=/usr/lib/openblas-base/
    export BUILD_VERSION=0.16.2
        
### Dependency
    <Home>
    sudo apt update

    <recomended>
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev libpng-dev;
    python3.8 -m pip install 'Cython<3'
    
    <option>
    sudo apt-get install libmpi-dev
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev
    
### Enviroment (below most in env directory)
    sudo apt install python3.8-venv;
    
    <masuk dalam enviroment>
    python3 -m venv yolov8_env;
    source yolov8_env/bin/activate;

## Check what in env PIP3
    python3.8 -m pip list

### LINK
https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048

Jetpack 5
PyTorch v2.1.0

    JetPack 5.1 (L4T R35.2.1) / JetPack 5.1.1 (L4T R35.3.1) / JetPack 5.1.2 (L4T R35.4.1)
        Python 3.8 - torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl 6.9k
python3.8 -m pip install --upgrade  pip
python3.8 -m pip install --update  pip

### TORCHVISION - 0.16.1
    
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev;
    <https://forums.developer.nvidia.com/t/cannot-compile-torchvision-0-16/289075/7>
    git clone --branch v0.16.1 https://github.com/pytorch/vision torchvision;  # ade yg buat jadi
    https://github.com/pytorch/vision torchvision <xpun download pastu paste kat home >
    cd torchvision
    export BUILD_VERSION=0.16.2; #check dalam version.txt
    python3.8 -m setup.py install --user;
    
### TORCH - 2.1.0
    <Goto link Download torch 2.1.0>
    cd Downloads; <atau paste ke Home>
    
    python3.8 -m pip install torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl;

    <atau>

    wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl -O torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl;
    sudo apt-get install python3-pip libopenblas-base libopenmpi-dev libomp-dev
    python3.8 -m pip install 'Cython<3'
    python3.8 -m pip install torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl;

    
### TEST TORCH with cuda

    python3.8 -c "import torch;print(torch.cuda.is_available())"

### YOLOv8
    hanya boleh guna code.py <download>
