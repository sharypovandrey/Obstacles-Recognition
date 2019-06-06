# Obstacles Recognition
## ROS package for obstacles detection using Stereo Camera, RK3399 and Tensorflow

`sudo pip install pyyaml`
### Install tesnorflow
https://docs.khadas.com/edge/InstallTensorFlow.html
```
sudo apt-get update
sudo apt-get install python-pip python-dev
```
Get TensorFlow Wheel for aarch64
Download TensorFlow wheel for aarch64 to someplace like:~/Downloads, we will download version 1.12.0
```
cd ~/Downloads
wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.12.0/tensorflow-1.12.0-cp27-none-linux_aarch64.whl
sudo pip install --ignore-installed tensorflow-1.12.0-cp27-none-linux_aarch64.whl # --ignore-installed solves problem with enum34
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```

### Install opencv
```
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

git clone https://github.com/opencv/opencv.git
cd opencv/
git checkout 3.2.0
cd ..
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib/
git checkout 3.2.0
cd opencv/
mkdir build
cd build/
export PY_NAME=$(python -c 'from sys import version_info as v; print("python%d.%d" % v[:2])')
export PY_NUMPY_DIR=$(python -c 'import os.path, numpy.core; print(os.path.dirname(numpy.core.__file__))')
cmake -DCMAKE_BUILD_TYPE=RELEASE \
-DCMAKE_INSTALL_PREFIX=/usr/local \
\
-DPYTHON2_EXECUTABLE=$(which python) \
-DPYTHON_INCLUDE_DIR=/usr/include/$PY_NAME \
-DPYTHON_INCLUDE_DIR2=/usr/include/aarch64-linux-gnu/$PY_NAME \
-DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/lib$PY_NAME.so \
-DPYTHON2_NUMPY_INCLUDE_DIRS=/usr/lib/$PY_NAME/dist-packages/numpy/core/include/ \
\
-DBUILD_DOCS=OFF \
-DBUILD_EXAMPLES=OFF \
-DBUILD_TESTS=OFF \
-DBUILD_PERF_TESTS=OFF \
\
-DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
..
make -j$(nproc --all)
sudo make install
```

Download this repo to your `cd ~/catkin_ws/src/ && git clone https://github.com/sharypovandrey/Obstacles-Recognition`

Rename it `mv Obstacles-Recognition-master obstacles_recognition`

## IMPORTANT:
Now path to the model is absolute:

`model = tf.keras.models.load_model('/home/firefly/catkin_ws/src/obstacles_recognition/model/model.h5')`

Please, change it to your Firefly's path

### Add package to your workspace

`cd ~/catkin_ws && catkin_make`

## Launch

`roslaunch obstacles_recognition obstacles.launch`

Subscribe to `/obstacles` topic

It gives 'yes' or 'no' (obstacle)
