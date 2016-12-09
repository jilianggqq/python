#!/bin/bash
PATH="$PATH:/usr/bin/"
export USER="itu"
DISPLAY1="6"
DISPLAY2="8"
DEPTH="24"
GEOMETRY="1366x768"
OPTIONS1="-depth ${DEPTH} -geometry ${GEOMETRY} :${DISPLAY1} -localhost"
OPTIONS2="-depth ${DEPTH} -geometry ${GEOMETRY} :${DISPLAY2} -localhost"
. /lib/lsb/init-functions

echo "set up ok."

case "$1" in
start)
	echo "Starting vncserver for user '${USER}' on localhost:${DISPLAY1}"
	vncserver ${OPTIONS1}
	echo "Starting vncserver for user '${USER}' on localhost:${DISPLAY2}"
	vncserver ${OPTIONS2}
	;;
stop)
	echo "Stopping vncserver for user '${USER}' on localhost:${DISPLAY1}"
	vncserver -kill :${DISPLAY1}
	echo "Stopping vncserver for user '${USER}' on localhost:${DISPLAY2}"
	vncserver -kill :${DISPLAY2}
	;;
restart)
	$0 stop
	$0 start
	;;
esac
exit 0