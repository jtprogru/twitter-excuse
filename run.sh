#!/bin/bash -
#===============================================================================
#
#          FILE: run.sh
#
#         USAGE: ./run.sh
#
#   DESCRIPTION: simple wrapper for my twitter autoposter
#
#       OPTIONS: ---
#  REQUIREMENTS: see Makefile
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: MICHAEL SAVIN (jtprogru), <jtprogru@gmail.com>
#  ORGANIZATION: SysOps
#       CREATED: 04/15/2021 21:07
#      REVISION:
#===============================================================================

set -e -o nounset                              # Treat unset variables as an error

DATE=$(LC_ALL="en_US.UTF-8"  date +"%Y-%m-%dT%H:%M")

SCRIPT=$(basename "$0")
LOG_FILE_NAME="twitterbot.log"

echo "${SCRIPT} ${DATE} Change directory" >> ${LOG_FILE_NAME}
cd ${WPDIRPY}/twitter-excuse/

echo "${SCRIPT} ${DATE} Loading enviroment" >> ${LOG_FILE_NAME}

# source ../venv/bin/activate

source .env

echo "${SCRIPT} ${DATE} Enviroment loaded" >> ${LOG_FILE_NAME}

echo "${SCRIPT} ${DATE} RUN!" >> ${LOG_FILE_NAME}

poetry run twit

echo "${SCRIPT} ${DATE} Done!" >> ${LOG_FILE_NAME}

# deactivate

exit 0

