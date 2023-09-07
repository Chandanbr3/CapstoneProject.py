import requests
from bs4 import BeautifulSoup

#URL = "https://www.amazon.in/Nokia-Android-Smartphone-Battery-Virtual/dp/B0C3J61K57/ref=sr_1_1?crid=125HMLRYU97FJ&keywords=deal%2Bprice%2Btoday%2Bmobile&qid=1694061561&sprefix=deal%2Bprice%2Btoday%2Bmobile%2Caps%2C351&sr=8-1&th=1"
URL ="https://www.amazon.in/Itel-5000mAh-Battery-Charging-Display/dp/B0C69Z421Z/ref=sr_1_5?crid=125HMLRYU97FJ&keywords=deal%2Bprice%2Btoday%2Bmobile&qid=1694061561&sprefix=deal%2Bprice%2Btoday%2Bmobile%2Caps%2C351&sr=8-5&th=1"
product_to_track = [
    {
        "product_url" : "https://www.amazon.in/Nokia-Android-Smartphone-Battery-Virtual/dp/B0C3J61K57/ref=sr_1_1?crid=125HMLRYU97FJ&keywords=deal%2Bprice%2Btoday%2Bmobile&qid=1694061561&sprefix=deal%2Bprice%2Btoday%2Bmobile%2Caps%2C351&sr=8-1&th=1",
        "name": " Nokia C12 pro android ",
        "target_price": 7000
    },


    {
       "product_url" : "https://www.amazon.in/Itel-5000mAh-Battery-Charging-Display/dp/B0C69Z421Z/ref=sr_1_5?crid=125HMLRYU97FJ&keywords=deal%2Bprice%2Btoday%2Bmobile&qid=1694061561&sprefix=deal%2Bprice%2Btoday%2Bmobile%2Caps%2C351&sr=8-5&th=1",
       "name" : "Itel s23",
        "target_price": 8700
    },

    {
        "product_url" : "https://www.amazon.in/Apple-iPhone-128GB-Deep-Purple/dp/B0BDJ6ZMCC/ref=sr_1_1_sspa?crid=188XWUHXI3RUG&keywords=iphone%2B14%2Bpro&qid=1694068326&sprefix=I%2Bphone%2B14%2Bpr%2Caps%2C362&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "name":"I phone 14",
        "target_price":120000
    },
    {
        "product_url":"https://www.amazon.in/IKALL-Z19-Pro-Smartphone-Multi-Touch/dp/B0C2CWV2PS/ref=sr_1_11_sspa?crid=I3TJW44A5KWW&keywords=samsung%2Bmobile&qid=1694072282&sprefix=samsung%2B%2Caps%2C328&sr=8-11-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1",
        "name" : "IKALL Z19 Pro",
        "target_price" : 7700
    },
    {
        "product_url":"https://www.amazon.in/OnePlus-Titan-Black-256GB-Storage/dp/B0BQJLVSC2/ref=sr_1_1?crid=NR06Z497NWIM&keywords=oneplus%2B11&qid=1694072496&sprefix=one%2Bpl%2Caps%2C345&sr=8-1&th=1",
        "name" : "One plus 11T",
        "target_price" : 62000

    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find(class_="a-price-whole")

    return product_price.getText()
Result_file =open("My_Result_file.txt","w")

try:
    for every_product in product_to_track:
        product_price_returned = give_product_price(every_product.get('product_url'))
        print(product_price_returned + "-" + every_product.get("name"))
        my_product_price = product_price_returned[0:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = float(my_product_price)
        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("available at your required Rate")
            Result_file.write(
                every_product.get("name") + '-\t ' + " available at Target price  "  +  " current price - " +  str(my_product_price)+'\n')
        else:
            print("still at your current price")
finally:
    Result_file.close()






