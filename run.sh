#!/usr/bin/env bash
D=$(LC_ALL="en_US.UTF-8"  date +"%Y-%m/%d:%H:%M")
set -e
SCRIPT=`basename "$0"`
echo "$SCRIPT $D Change directory" >> /Users/jtprog/workplace/logs/twitterbot.log
cd /Users/jtprog/workplace/python/twitter-excuse/

echo "$SCRIPT $D Loading enviroment" >> /Users/jtprog/workplace/logs/twitterbot.log
source ./venv/bin/activate
echo "$SCRIPT $D Enviroment loaded"  >> /Users/jtprog/workplace/logs/twitterbot.log
source ./.env
echo "$SCRIPT $D RUN!" >> /Users/jtprog/workplace/logs/twitterbot.log
python3 ./src/main.py
echo "$SCRIPT $D Done!" >> /Users/jtprog/workplace/logs/twitterbot.log
deactivate
