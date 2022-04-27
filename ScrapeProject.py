import requests
from bs4 import BeautifulSoup

### Must use request in order to be able to parse over a website's HTML.
Site1 = requests.get("https://www.newegg.com/black-red-blue-nintendo-hadskabaa-switch-console-with-neon-blue-and-neon-red-joy-con/p/N82E16878190842?Description=nintendo%20switch%20console&cm_re=nintendo_switch%20console-_-78-190-842-_-Product")
Site2 = requests.get("https://www.ebay.com/p/16029037217?iid=384802587018")
Site3 = requests.get("https://www.rcwilley.com/Electronics/Gaming/Nintendo-Switch/SWI-HEGSKABAA/112465749/Nintendo-Switch-OLED-Model-With-Neon-Red-and-Neon-Blue-Joy-Con-View")

### Beautiful Soup is a Python library used for scraping XML and HTML files.
SP1 = BeautifulSoup(Site1.content, 'html.parser')
SP2 = BeautifulSoup(Site2.content, 'html.parser')
SP3 = BeautifulSoup(Site3.content, 'html.parser')

### To find the appropriate data, in this case, the price must be parsed, and this is accomplished by finding its element.
PriceSite1 = SP1.find('li','price-current')
PriceSite2 = SP2.find('div','display-price')
PriceSite3 = SP3.find('span','price')

### Once the information is scraped, the .strip() method is used to take away the "$" to ensure the output is consistent.
PriceOnNeweeg = PriceSite1.get_text().strip('$')
PriceOnEbay = PriceSite2.get_text().strip('$')
PriceRcwilley = PriceSite3.get_text()

# Adding Price on ____ to clarify the website
Newegg = "Price on Newegg : " + str(PriceOnNeweeg)
eBay = "Price on eBay : " + str(PriceOnEbay)
Rcwilley = "Price on RC Willey : " + str(PriceRcwilley)

### = Saving the outputs as a common variable.
Prices = Newegg, eBay, Rcwilley

### Printing the prices scraped off of Newegg, eBay, and RC Willey.
print(Prices)


