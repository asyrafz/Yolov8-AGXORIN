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
    export BUILD_VERSION=0.16.1
        
### Dependency
    <Home>
    sudo apt update

    <recomended>
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev libpng-dev;
    pip3 install 'Cython<3'
    
    <option>
    sudo apt-get install libmpi-dev
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev
    
### Enviroment (below most in env directory)
    sudo apt install python3.8-venv;
    python3 -m venv yolov8_env;
    source yolov8_env/bin/activate;

## Check what in env PIP3
    pip3 list

### LINK
https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048

Jetpack 5
PyTorch v2.1.0

    JetPack 5.1 (L4T R35.2.1) / JetPack 5.1.1 (L4T R35.3.1) / JetPack 5.1.2 (L4T R35.4.1)
        Python 3.8 - torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl 6.9k

### TORCHVISION - 0.16.1
    git clone --branch v0.16.1 https://github.com/pytorch/vision torchvision

    cd torchvision
    
    export BUILD_VERSION=0.16.1
    python3 setup.py install --user 

    <atau>
    pip3 install -v torchvision==0.16.1

    <atau>
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev;
    git clone --branch v0.16.1 https://github.com/pytorch/vision torchvision;
    cd torchvision
    export BUILD_VERSION=0.16.1;
    python3 setup.py install --user;
    
    
### TORCH - 2.1.0
    <Goto link Download torch 2.1.0>
    cd Downloads;
    
    pip3 install torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl;

    <atau>
    wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl -O torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl;
    pip3 install numpy torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl
    
    <try>
    wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl -O torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl;
    sudo apt-get install python3-pip libopenblas-base libopenmpi-dev libomp-dev
    pip3 install 'Cython<3'
    pip3 install numpy torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl;
    
    
###TEST TORCH with cuda
    import torch;
    print(torch.cuda.is_available())

    <check if it true>


### YOLOv8
    git clone https://github.com/ultralytics/yolov8.git
    cd yolov8
    git checkout v8.0
    pip3 install -r requirements.txt

    <Test>
    pip3 install ultralytics
    yolo task=detect mode=predict model=yolov8n.pt source=0 show=true
