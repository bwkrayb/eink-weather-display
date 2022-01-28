#!/bin/bash
export EINK_HOME='/home/pi/eink-2in7'
cd $EINK_HOME
nohup /usr/bin/python3 $EINK_HOME/open-weather.py > $EINK_HOME/logs/start.out 2>&1 &
