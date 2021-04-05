#!/usr/bin/env bash
D=$(LC_ALL="en_US.UTF-8"  date +"%Y-%m-%dT%H:%M")
set -e
SCRIPT=`basename "$0"`
LOG_FILE_NAME="twitterbot.log"

echo "$SCRIPT $D Change directory" >> $MYLOGDIR/$LOG_FILE_NAME
cd $WPDIRPY/twitter-excuse/

echo "$SCRIPT $D Loading enviroment" >> $MYLOGDIR/$LOG_FILE_NAME
source ./venv/bin/activate
echo "$SCRIPT $D Enviroment loaded"  >> $MYLOGDIR/$LOG_FILE_NAME
source ./.env
echo "$SCRIPT $D RUN!" >> $MYLOGDIR/$LOG_FILE_NAME
python3 ./src/main.py
echo "$SCRIPT $D Done!" >> $MYLOGDIR/$LOG_FILE_NAME
deactivate
