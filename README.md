Blocket_project
===============

Scraping classifieds service blocket.se for car information. Scraped data is cleaned and 
saved in MongoDB. 

## Installation
`
$ pip install -r requirements.txt
`

## Usage
Set MongoDB credentials in `settings.py` and run 

`
$ scrapy crawl collect_cars
`