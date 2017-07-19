#!/usr/bin/env python
################################################################
## AUTHOR: Robert Markoski - 2017
## VERSION: 0.1
## LICENSE: GPL 3 [https://www.gnu.org/licenses/gpl.html]
## VERSION-INFO:
##      0.1     Initial Release. i.e. It Works!
################################################################

import subprocess
from ISStreamer.Streamer import Streamer

#--------SETTINGS---------
BUCKET_NAME = "Speedtest Results"
BUCKET_KEY = "speedtest"
ACCESS_KEY = "YOUR INITIAL STATE ACCESS KEY GOES HERE"

#-------------------------

def get_speeds():
    """Function Runs Speedtest and then gets updates"""
    speedtest = subprocess.check_output(['speedtest-cli']).split() #Rip apart the output
    results = list(speedtest[i] for i in [23, 29, 35]) # Get Ping, Download, Upload
    return results


speed = get_speeds()

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
streamer.log("Ping",speed[0])
streamer.log("Download",speed[1])
streamer.log("Upload",speed[2])
