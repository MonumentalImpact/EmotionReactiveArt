#installation

#first set up a virtual environment with

!python3 -m venv era #or whatever name you want to use era=emotion-reactive art
!source era/bin/activate

#then you can install the packages we need

!pip install deepface

!pip install tf-keras

!pip install thonny

To test the installation, open 'dftest.py' in the 'test' folder using thonny.
Run dftest.py.
This will download a bunch of data when you run it the first time.

for mqtt support, install mosquitto
!sudo apt install mosquitto

for dev purposes, add the following lines to /etc/mosquitto/mosquitto.conf

listener 1883
allow_anonymous true

Don't use this in production! This just makes it easier when in development.

run the server with:

!sudo mosquitto -c /etc/mosquitto/mosquitto.conf

send test messages with
!mosquitto_pub -t art/emotion -m test

