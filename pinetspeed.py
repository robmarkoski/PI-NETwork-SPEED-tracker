#!/usr/bin/env python
################################################################
## AUTHOR: Robert Markoski - 2017
## VERSION: 0.2
## LICENSE: GPL 3 [https://www.gnu.org/licenses/gpl.html]
## VERSION-INFO:
##      0.2     Added ability to select Bytes or Bits, and now only asking for
##              simplified output.
##      0.1     Initial Release. i.e. It Works!
################################################################

import subprocess
from ISStreamer.Streamer import Streamer

#--------SETTINGS---------
BUCKET_NAME = "Speedtest Results"
BUCKET_KEY = "speedtest"
ACCESS_KEY = "YOUR INITIAL STATE ACCESS KEY GOES HERE"

BYTES = 0 # Set to 1 if want to use MBytes/s rather than Mbits/s
#-------------------------

def get_speeds():
    """Function runs speedtest and splits out the results"""
    speedtest_args = "--simple --bytes" if BYTES == 1 else "--simple" #Determine arguments.
    speedtest = subprocess.check_output(["speedtest-cli", speedtest_args]).split() #Get Output.
    results = list(speedtest[i] for i in [1, 4, 7]) # Get Ping, Download, Upload
    return results


speed = get_speeds()

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
streamer.log("Ping",speed[0])
streamer.log("Download",speed[1])
streamer.log("Upload",speed[2])
