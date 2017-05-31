#!/bin/bash
#written by Liran Farage
#18/3/2017
#This script gets a directory with files and rename all of them to <number>.apk while number is an integer starting from
# *count* variable value

count=1

#validate passed argument as a directory
if [ ! -d "$1" ]; then
	echo "error:  $1 is not a directory"
	echo "exiting..."
	exit
fi

#change current path
cd $1

#iterate over the files and renaming them
for file in * ; do
	mv "$file" "${count}.apk"
	count=$((count + 1))
done
