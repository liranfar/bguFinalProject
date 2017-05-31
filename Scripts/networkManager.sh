#!/usr/bin/expect -f


set num [lindex $argv 0];

spawn ssh osboxes@192.168.56.101
#set arg1 [lindex $argv 0]
#send "echo sadasd $arg0"
expect "password:"
sleep 5
send "osboxes.org\r"
#echo "configuring ip address..."
expect "osboxes"
sleep 5
#send "echo '$((101+$num))'"
#send "echo num is : $((101+$num))"
#send "echo $count"
send {sudo sed -i -e 's/192.168.56.101/192.168.56.}
send "$num"
send {/g' /etc/NetworkManager/system-connections/university_network}
send "\r"
expect "password"
send "osboxes.org\r"
sleep 5
#expect "password"
#send "osboxes.org\r"
#sleep 5
#send "echo blabla"
exit
interact





