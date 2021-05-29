# Get your covid-meeting earlier

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

## Why
When booking my SARS-CoV-2 vaccine appointment in switzerland, I realized there were some frictions in the process:
* One can book several appointment dates
* One can delete an appointment at any moment
* There is a long wait to get the first vaccine

This mean some people will take several appointments and may delete then last minute (i.e. when receiving the 24h before recall).
To avoid waisting appointment slots (and doses), I created this simple web scrapper. 
As in Switzerland each vaccination center has its own online platform to do online appointments, this web scarper could not be generalized. You will thus have to modify it if you want to make it work on a specific website. <br>
Below you will find *how* to make the scraper work and *what* to change to make it work for you vaccination center.

**Disclaimer**: I added a sleep time in this web scraper to avoid overloading the servers. Please do not reduce this sleep time as the consequences of shutting down these websites could be disastrous. 

## How to make it work
### Downloads
**Git**<br>
To install this repository on your local computer:
* Change the current working directory to the location where you want the cloned directory.
* run $ git clone https://github.com/Labulitiolle/covid_meeting_scrapper.git <br>

**Python**<br>
This web-scraper is built in python.
You will thus need to have python installed locally. <br>
**Packages**<br>
The scraper uses [Selenium] (https://selenium-python.readthedocs.io/installation.html#introduction), a java bases library adapted for python. <br>
To install the requirements, open your terminal , navigate to this repository and run:
```shell
$ pip install -r requirements.txt
```

_Note_: Selenium was initially designed for functional/acceptance test, but for this simple application it makes the job.<br>
**Driver**<br>
For Selenium to work you need to install a web-driver. I used the Chrome driver, you can download it [here](https://chromedriver.chromium.org). 
Once it is downloaded, place it into the `Driver` folder in this repository.<br>
**Run** <br>
To run the web-scraper as I have built it run:
```shell
$ python covid_scrapper.py
```
The program will trigger an alarm (loud sound) once it has found a date earlier than teh 25th of June. 

## What to change
**Use the link of your website** <br>
Go to the website on which you want to take your appointment and whenever you reach the page where you can see the first available appointment. Copy the url and change line 72 to:
```python
s = Scraper(url=<your_url>)
```
**Find the xpath of the text** <br>
On any browser, you can see the source code of the web page. Navigate to the text showing the first available date and copy its xpath. Then replace line 18 as:
```python
self.text_xpath = "<your_xpath>"
```

**Reload page** <br>
On the website scrapped in the example of this script, whenever the page was reloaded, I had to click on a button to see the first available appointment. If this is not the case for your website you can comment out line 55.
Otherwise, adapt line 17 with the corresponding x_path.


# License
Public