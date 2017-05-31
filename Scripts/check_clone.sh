#!/bin/bash

	set -x
	echo "connecting via ssh"
	#sleep 20
	./interfaces.sh $((102))
	./networkManager.sh $((102))
