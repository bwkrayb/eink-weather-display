#!/bin/bash
cd /home/pi/eink-2in7/logs
cp eink.log eink.log.$(date +%m-%d-%T)
rm eink.log
