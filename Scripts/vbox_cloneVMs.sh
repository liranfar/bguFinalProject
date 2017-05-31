#!/bin/bash

#This script gets a VM, cloning it x times, generating and assigning sequential ip address to them

# set command tracing on
#set -x


if ! vboxmanage showvminfo $1 --machinereadable >/dev/null 2>&1 ;then
	echo "error: $1 VM not found"
	echo "usage <machine_name> <path_to_cuckoo dir>"
	exit 1;	
fi

echo "found machine: $1"

echo "enter number of clones..."
read number_of_clones


echo "starting cloning..."

spinner() {
	chars="/-\|"

	while :; do
	  for (( i=0; i<${#chars}; i++ )); do
		sleep 0.5
		echo -en "${chars:$i:1}" "\r"
	  done
	done
}

trap ctrl_c INT

function ctrl_c() {
        echo "** Trapped CTRL-C"
		exit 1
}

#running spinner thread command
#spinner &	


for (( i=1; i<=$number_of_clones; i++ )) ; do
	copy="_copy_$i"
	echo "cloning #$i..."
	vboxmanage clonevm "$1" --name "$1$copy" 
	vboxmanage registervm ~/VirtualBox\ VMs/"$1$copy"/"$1$copy".vbox >/dev/null 2>&1
	echo "starting vm..."
	vboxheadless -s "$1$copy">/dev/null&
	while ! VBoxManage list runningvms | grep --quiet "$1$copy" ;do
	echo -n "."
	sleep 1
	done
	echo ""
	echo "connecting via ssh"
	sleep 20
	./interfaces.sh $((101+$i))
	./networkManager.sh $((101+$i))
	#./interfaces "$((101+$i))"
	echo "
[$1$copy]
label = $1$copy
platform = android_on_linux
ip = 192.168.56.$(( 101 + $i ))
">> "$2/cuckoo/conf/virtualbox.conf"
	sed -i "/machines =/s/$/ ,$1$copy/" $2/cuckoo/conf/virtualbox.conf
	echo "finished cloning #$i"
	echo "creating a snapshot..."
	VBoxManage snapshot "$1$copy" take "$1$copy"_snapshot
	echo "Shutting down VM..."
	VBoxManage controlvm "$1$copy" poweroff
	VBoxManage snapshot "$1$copy" restore "$1$copy"_snapshot
done


#kill "$!" #kill the spinner

echo "cloning done!"
