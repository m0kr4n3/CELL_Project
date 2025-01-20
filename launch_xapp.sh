#!/bin/bash

echo "Starting xApp..."
sudo /home/cell/flexric/build/examples/xApp/c/monitor/xapp_kpm_moni


sudo kill -9 `pgrep 'xapp'`
