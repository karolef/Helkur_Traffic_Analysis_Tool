#!/bin/bash

#traf="/home/karol/traffic_scraper/traffic"

minutes=`date '+%Y_%m_%d__%H_%M'`
today=`date '+%Y_%m_%d__%H_%M_%S'`

mkdir /home/karol/traffic_scraper/traffic_pcap-$minutes
cd /home/karol/traffic_scraper/traffic_pcap-$minutes

sudo tcpdump -vv -s 0 -C 1 -c 5000 -w traffic

files=$(ls -1 | wc -l)
file_count=$(($files-1))
START=0
#echo $file_count
for (( i=$START; i<=$file_count; i++))
do
	if [ $i = 0 ]
	then
		tshark -r traffic -T fields -E separator=, -E quote=d -e frame.time_epoch -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e _ws.col.Protocol -e frame.len > outfile-$today.csv
	else
		tshark -r traffic$i -T fields -E separator=, -E quote=d -e frame.time_epoch -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e _ws.col.Protocol -e frame.len > outfile$i-$today.csv
	fi
done

sudo zip full_traffic-$today.zip outfile*.csv

sudo cp full_traffic-$today.zip /srv/ftp/
