#!/bin/bash  

current_dir=$(dirname "${BASH_SOURCE[0]}")
export PYTHONPATH="$current_dir/../splunk_sdk-1.3.1-py2.7.egg"
echo "PYTHONPATH=$PYTHONPATH"
python "$current_dir/test_validation.py" $@
