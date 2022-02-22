#!/bin/bash

power () {
	echo - | awk "{printf \"%.6f\", 	$(( 	  $(cat /sys/class/power_supply/BAT1/current_now) * 	  $(cat /sys/class/power_supply/BAT1/voltage_now) 	)) / 1000000000000 }"
}

echo ",W"
i=0
polling=${1:-1}    
while true
do
	sleep $polling
	echo "$i,$(power)"
	i=$((i+1))
done
