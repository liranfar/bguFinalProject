#!/bin/bash
set +x
export PATH=$PATH:/home/osboxes/Desktop/tool:/home/osboxes/Desktop/build-tools/25.0.2/:/home/osboxes/Desktop/platform-tools

echo "checking if device is running..."
if [ "`adb shell getprop sys.boot_completed | tr -d '\r' `" != "1" ] 
then 
	echo "device is offline... starting."
	gnome-terminal -e '/home/osboxes/Desktop/prepareGuestScripts/run_emulator.sh'
else
	echo "device is up"
fi

echo "waiting for device..."
while [ "`adb shell getprop sys.boot_completed | tr -d '\r' `" != "1" ] ; do sleep 5;echo -n "."; done

echo "intializing device..."
cd ~/Desktop/cuckoo/utils/android_emulator_creator
./create_guest_android_on_linux.sh

echo "executing xposed installer"
adb shell monkey -p de.robv.android.xposed.installer -c android.intent.category.LAUNCHER 1 
sleep 20
echo "framework" 
adb shell input tap 189 302 
sleep 15
echo "install/update"
adb shell input tap 230 510
sleep 20
echo "no"
adb shell input tap 119 598
sleep 15
echo "soft reboot"
adb shell input tap 230 630
sleep 15
echo "yes"
adb shell input tap 350 500
sleep 15

echo "waiting for device..."
while [ "`adb shell getprop sys.boot_completed | tr -d '\r' `" != "1" ] ; do sleep 5;echo -n "."; done

echo "device is ready!"

cd ~/Desktop/cuckoo/agent

echo "starting agent..."
python agent.py
