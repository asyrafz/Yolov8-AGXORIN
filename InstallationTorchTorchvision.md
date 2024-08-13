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

### install Visual Studio Code

[<kbd> <br> Vscode installer <br> </kbd>][https://vscode.download.prss.microsoft.com/dbazure/download/stable/eaa41d57266683296de7d118f574d0c2652e1fc4/code_1.92.1-1723064751_arm64.deb]

    sudo apt install ./code_1.92.1-1723064751_arm64.deb

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

    
### Enviroment (below most in env directory)
    sudo apt install python3.8-venv;
    
<masuk dalam enviroment>
    python3.8 -m venv yolov8_env;
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

### TORCH - 2.1.0
    https://developer.download.nvidia.cn/compute/redist/jp/v512/pytorch/torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl

    sudo apt-get install python3-pip libopenblas-base libopenmpi-dev libomp-dev libjpeg-turbo
    
    pip3 install 'Cython<3'

    pip3 install numpy torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl

### TORCHVISION - 0.16.1
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev

< Y capital not y >

    git clone --branch v0.16.1 https://github.com/pytorch/vision torchvision

    cd torchvision

    export BUILD_VERSION=0.16.1

    python3 setup.py install --user

    cd ../

### TEST TORCH with cuda

    python3.8 -c "import torch;print(torch.cuda.is_available())"

### YOLOv8
    pip3 install ultralytics
