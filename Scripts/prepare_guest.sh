#!/bin/bash

set +x
echo "running the emulator.."
gnome-terminal -x sh --working-directory=/home/osboxes/Desktop/tools/  -c  './emulator -avd aosx -qemu -nand -system,size=0x1f400000,file=/home/osboxes/Desktop/system-images/android-16/default/armeabi-v7a/system.img;exec bash'

echo"configuring PATH..."
export PATH=$PATH:/home/osboxes/Desktop/tool:/home/osboxes/Desktop/build-tools/25.0.2/:/home/osboxes/Desktop/platform-tools

echo "installing deamon"
cd /Desktop/cuckoo/utils/android_emulator_creator
./create_guest_android_on_linux.sh 

echo "starting agent"
cd /Desktop/cuckoo/agent
python agent.py
