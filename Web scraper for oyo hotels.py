
import requests
from bs4 imports Beautiful Soup
Import pandas 

Req= requests.get (oyo_url)
Content=req.content

Soup= Beautiful Soup (content, "html.parser")
all hotels = soup.find_all (" div",("class":"hotelcardlisting") )
scaped_info_list =[ ]
Oyo_url = "https:// www.oyorooms.com/hotels-in-bangalore"
For hotel in all _hotels :
       hotel_ dict = { }
       hotel_ dict [ " name "] = hotel .find ("h3", {"class": " listinghotelDescription_ho}
hotel_dict["address"] = hotel. find("span", ("intemprop": "StreetAddress" ]).te
hotel_dict["price"] = hotel.find ("span", {"class": "listingprice_finalprice

#try...... except
try:
      hotel_dict["rating"] = hotel.find("div", {"class": "amenitywrapper"} )
except Attribute Error:
         Pass
data frame = pandas .Data frame (scraped_info_list)
#dataframe.to_csv ("oyo.csv")
Print (name, address, price, rating)
