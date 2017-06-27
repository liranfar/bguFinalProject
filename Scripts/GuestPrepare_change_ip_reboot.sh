#!/bin/bash
cd /home/osboxes/Desktop/tools/
./emulator -avd aosx -qemu -nand -system,size=0x1f400000,file=/home/osboxes/Desktop/system-images/android-16/default/armeabi-v7a/system.img&
read line
