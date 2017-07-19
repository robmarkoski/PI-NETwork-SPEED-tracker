# PI NETwork SPEED tracker

Keep your ISP in check and ensure your getting the speeds you paid for. This script when run will log your current network performance (ping time, download and upload speeds) to an Initialstate bucket. Run it on an hourly schedule to get a running stream of your network performance.

## Getting Started

This script is painfully easy to get up and running.

### Prerequisites

You will need to have an Initialstate account and have the python libaries installed. [See Here](https://github.com/InitialState/wunderground-sensehat/wiki/Part-1.-Initial-State) 

Net you also need [speedtest-cli](https://github.com/sivel/speedtest-cli) installed.

```
pip install speedtest-cli
```

### Installing

Copy the script someone onto your device. 
```
git clone https://github.com/robmarkoski/PI-NETwork-SPEED-tracker
```

Schedule it to run hourly with cron

```
crontab -e
```
Then add the following to run it on the hour every hour.

```
0 * * * * /location/of/script/pinetspeed.py
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system


## Authors

* **Rob Markoski** - [GitHub](https://github.com/robmarkoski)



## License

This project is licensed under the GPL3 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Initialstate](https://www.initialstate.com)
* Sivel - [Speedtest-Cli](https://github.com/sivel/speedtest-cli)
