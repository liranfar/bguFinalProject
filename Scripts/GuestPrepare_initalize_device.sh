#!/bin/bash
export PATH=$PATH:/home/osboxes/Desktop/tool:/home/osboxes/Desktop/build-tools/25.0.2/:/home/osboxes/Desktop/platform-tools
while [ "`adb shell getprop sys.boot_completed | tr -d '\r' `" != "1" >/dev/null&] ; do sleep 5; done
cd /Desktop/cuckoo/utils/android_emulator_creator
./create_guest_android_on_linux.sh
cd /Desktop/cuckoo/agent
python agent.py
