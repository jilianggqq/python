#!/bin/bash
# $# The $# variable will tell you the number of input arguments the script was passed.
# echo $#
if [ $# -eq 0 ];then
    source ~/MyProjects/nodejs/vir_env/bin/activate
    source ~/MyProjects/nodejs/vir_nodeenv/bin/activate
elif [[ "$1" -eq "-d" ]]; then
    #statements
    # $1 is the first paramter in the command line.
    # echo $1
    deactivate
fi

#sudo ln -sf ~/MyProjects/python/scripts/shell/acti.sh /usr/local/bin/acti

