from bs4 import BeautifulSoup
import smtplib
import requests
import os
from dotenv import load_dotenv

load_dotenv()

ITEM_URL = "https://www.amazon.de/gp/product/B0BYZFF7HT/ref=ox_sc_saved_title_1?smid=A1ZKU0MQBS8OBB&th=1"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
EMAIL = os.getenv('EMAIL')
PSWRD = os.getenv('PSWRD')

response = requests.get(url=ITEM_URL, headers=HEADERS)
content = response.text

soup = BeautifulSoup(content, "html.parser")

# print(soup.prettify())

# Now try to get that value
element = soup.find('input', attrs={'name': 'items[0.base][customerVisiblePrice][amount]'})
if element:
    value = element.get('value')
    if float(value) < 50:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PSWRD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="uncle.underhill@gmail.com",
                msg=f"Subject: Price alert!\n\n "
                    f"Your desired item is now being sold for only {value} euro."
                    f"If you still want to buy it you should visit {ITEM_URL}"
                    f"Cheers")
else:
    print("Element not found")
