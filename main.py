import requests
from bs4 import BeautifulSoup
import smtplib

price_margin=100

email="*****@gmail.com"
password="PASSWORD"

url="https://www.amazon.com/dp/B08CFZF16Y/ref=sbl_dpx_kitchen-electric-cookware_B08CFZF16Y_0"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

response=requests.get(url,headers=header)
website=response.text

soup=BeautifulSoup(website,"lxml")
# print(soup.prettify())
price=soup.select(".a-price-whole")[0].getText()
price_as_float=float(price)
print(price_as_float)

title=soup.find(id="productTitle").get_text().strip()
print(title)
if price_as_float<price_margin:
    message=f"{title} is now at {price}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="anushka1209rv@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
                            )

