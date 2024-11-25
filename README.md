## CoinCap Restful API automated data collection 

### Requirements (Modules)

* argparse
* configparser
* datetime
* requests
* shutil

### Parser details

**Description: The data will be first loaded to a Flat File**

* **-s:** The section name of configuration file, which will be used to get the object information.

* **-a:** The asset name which will be used to get the object information.

* **-sd:** The Start date which will be use to get the object information. Default Start date is today minus three days

* **-ed:** The End date which will be use to get the object information. Default End date is current datetime

* **-it:** The interval which will be use to get the object information. Default interval is m30, m = minute, h = hour and d = day
    * m1: 1 minute interval
    * m5: 5 minute interval
    * m15: 15 minute interval
    * m30: 30 minute interval
    * h1: 1 hour interval
    * h2: 2 hour interval
    * h6: 6 hour interval
    * h12: 12 hour interval
    * d1: 1 day interval

* **-l:** Logging level, "info" by default.
    * info
    * debug
    * warning
    * error

* **-p:** The configuration file to be used. If not specified, the program will try to find it with "./config.ini"

* **--print_log:** Whether print the log to console. False by default


### Example Execution:

* **Asset: python3** controller.py -s ASSET -a solana -l info --print_log True

* **Asset_History** (Default Start/End): python3 controller.py -s ASSET_HISTORY -a bitcoin -it m30 -l info

* **Asset_History:** python3 controller.py -s ASSET_HISTORY -a bitcoin -it m30 -sd 2024-11-01T00:00:00Z -ed 2024-11-01T23:59:59Z -l info

* **ASSET_MARKETS:** python3 controller.py -s ASSET_MARKETS -a bitcoin -l info

* **EXCHANGES:** python3 controller.py -s EXCHANGES -a binance -l info

* **RATES:** python3 controller.py -s RATES -a bitcoin -l info

* **MARKETS:** python3 controller.py -s MARKETS -a '' -l info