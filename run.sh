#!/usr/bin/env bash
DATE=$(LC_ALL="en_US.UTF-8"  date +"%Y-%m-%dT%H:%M")
set -e
SCRIPT=`basename "$0"`
LOG_FILE_NAME="twitterbot.log"

export MYLOGDIR=/Users/jtprog/workplace/logs
export WPDIRPY=/Users/jtprog/workplace/python

echo "${SCRIPT} ${DATE} Change directory" >> ${MYLOGDIR}/${LOG_FILE_NAME}
cd ${WPDIRPY}/twitter-excuse/

echo "${SCRIPT} ${DATE} Loading enviroment" >> ${MYLOGDIR}/${LOG_FILE_NAME}
source ./venv/bin/activate
echo "${SCRIPT} ${DATE} Enviroment loaded"  >> ${MYLOGDIR}/${LOG_FILE_NAME}
source ./.env
echo "${SCRIPT} ${DATE} RUN!" >> ${MYLOGDIR}/${LOG_FILE_NAME}
python3 ./src/main.py
echo "${SCRIPT} ${DATE} Done!" >> ${MYLOGDIR}/${LOG_FILE_NAME}
deactivate
