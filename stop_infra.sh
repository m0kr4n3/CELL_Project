#!/bin/bash

echo "Stopping gNodeB..."
echo "Stopping UE..."
sudo kill -9 `pgrep nr-softmodem`

echo "Stopping RIC..."
sudo kill -9 `pgrep near`

echo "Stopping 5G Core Network..."
cd /home/cell/lab8
sudo docker-compose -f docker-compose-5g-core.yaml down
