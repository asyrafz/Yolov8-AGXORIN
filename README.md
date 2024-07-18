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

## LINK
https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048

PyTorch v2.1.0

    JetPack 5.1 (L4T R35.2.1) / JetPack 5.1.1 (L4T R35.3.1) / JetPack 5.1.2 (L4T R35.4.1)
        Python 3.8 - torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl 6.9k
        
### Dependency

    sudo apt-get install libmpi-dev

    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
    
    sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev <option>

### Path reg


### TORCH 
pip3 install torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl
    
