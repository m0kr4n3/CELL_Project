#!/bin/bash


echo "Starting 5G Core Network..."
cd /home/cell/lab8
sudo docker-compose -f docker-compose-5g-core.yaml up -d
echo -e "\n"

echo "Starting gNodeB..."
sudo ~/openairinterface5g/cmake_targets/ran_build/build/nr-softmodem -O /home/cell/lab8/flexric_conf/gnb.conf  --gNBs.[0].min_rxtxtime 6 --rfsim >> /tmp/gnb.log 2>&1 &
sleep 20
echo -e "\n"

echo "Starting UE..."
sudo /home/cell/openairinterface5g/cmake_targets/ran_build/build/nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --rfsim -O /home/cell/lab8/ran-conf/nr-ue.conf >> /tmp/ue.log 2>&1 &
sleep 10
echo -e "\n"

echo "Starting RIC..."
sudo /home/cell/flexric/build/examples/ric/nearRT-RIC >> /tmp/ric.log 2>&1 &
echo -e "\n"

