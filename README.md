# mu5735

ADS-B data, graphs and basic analysis for the crash of [Chinese Eastern Flight 5735](https://en.wikipedia.org/wiki/China_Eastern_Airlines_Flight_5735), collected from flightradar24 ([granular data](https://www.flightradar24.com/blog/china-eastern-airlines-flight-5735-crashes-en-route-to-guangzhou/), [detailed data](https://twitter.com/flightradar24/status/1505863117343014916/photo/2), [coarse data](https://www.flightradar24.com/data/aircraft/b-1791#2b367bc1)).

For educational purposes only.

[Download KML](https://github.com/cathaypacific8747/mu5735/releases/download/v0.1/MU5735-Flightradar24-Granular-Data.kml)

To generate KML:
```
$ sudo apt-get install python3-lxml
$ pip3 install urllib3 pandas fastkml shapely colour
$ python3 coarse.py # download data from fr24, save to data/coarse.csv
$ python3 kml.py    # process data from data/combined.csv, output KML
```

## Additional information from CAAC Preliminary Report

[Source](http://www.caac.gov.cn/XXGK/XXGK/TZTG/202204/t20220420_212895.html)

`14:20:55` - Guangzhou FIR radar indicates "deviation from assigned altitude", no response from flight crew

`14:21:40` - Final radar contact: ALT - 3380m/11089ft, GS - 1010kmh/545kt, HDG - 117

## Flight Path

Towards east:
![east](img/east_view.png)

Towards west:
![west](img/west_view.png)

Top view:
![top](img/top_path.png)

Entire path:
![entire](img/entire_path.png)

## Flight Parameter changes before crash

![altitude](img/altitude.png)
![speed](img/speed.png)
![verticalspeed](img/vertical_speed.png)
![heading](img/heading.png)