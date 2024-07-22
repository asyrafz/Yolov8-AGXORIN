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

## LINK
https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048

PyTorch v2.1.0

    JetPack 5.1 (L4T R35.2.1) / JetPack 5.1.1 (L4T R35.3.1) / JetPack 5.1.2 (L4T R35.4.1)
        Python 3.8 - torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl 6.9k

### Path reg
    sudo apt update
    
    sudo apt-get install nano
    
    nano /home/$USER/.bashrc

    export PATH=/usr/local/cuda-11.4/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64:$LD_LIBRARY_PATH
    
    export PATH=/home/agx_orin/.local/bin:$PATH
    export LD_LIBRARY_PATH=/usr/lib/openblas-base/
    export BUILD_VERSION=0.16.1
        
### Dependency
    <Home>
    sudo apt update

    <recomended>
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev
    pip3 install 'Cython<3'
    
    <option>
    sudo apt-get install libmpi-dev
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev

    
    python3 setup.py install --user
    
### TORCH - 2.1.0
    <Home>
    
    pip3 install torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl


### TORCHVISION - 0.16.1
    git clone --branch v0.16.1 https://github.com/pytorch/vision torchvision

    cd torchvision

    python3 setup.py install --user

### YOLOv8
    git clone https://github.com/ultralytics/yolov8.git
    cd yolov8
    git checkout v8.0
    pip3 install -r requirements.txt

    <Test>
    yolo task=detect mode=predict model=yolov8n.pt source=1 --show=true
