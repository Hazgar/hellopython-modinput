@SET "PYTHONPATH=%~dp0\app\splunk_sdk-1.3.1-py2.7.egg"
@"%SPLUNK_HOME%"\bin\splunk cmd python "%~dp0\app\hellopython.py" %*
