#!/bin/bash  

current_dir=$(dirname "$0")
PYTHONPATH="$current_dir/app/splunk_sdk-1.3.1-py2.7.egg"
"$SPLUNK_HOME/bin/splunk" cmd python "$current_dir/app/hellopython.py" $@
