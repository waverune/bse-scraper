import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

# read the html file (implement read fromn site)
url = 'https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

html_text = requests.get(
    url, headers=headers)

soup = BeautifulSoup(html_text.content, 'lxml')

# init lists
Date = []
Code = []
SecName = []
Name = []
Type = []
Quantity = []
Price = []

# parse the td tags in sequence
j = 0
td_tags = soup.find_all(
    'td', class_=['tdcolumn', 'tdcolumn text-right', 'TTRow_left'])
for info in td_tags:
    if (j % 7) == 1:
        Date.append(info.text)
    if (j % 7) == 2:
        Code.append(info.text)
    if (j % 7) == 3:
        SecName.append(info.text)
    if (j % 7) == 4:
        Name.append(info.text)
    if (j % 7) == 5:
        Type.append(info.text)
    if (j % 7) == 6:
        Quantity.append(info.text)
    if (j % 7) == 0:
        Price.append(info.text)

    j = j+1

print("^^^^^^^^^^^^")

df = pd.DataFrame({
    'Deal Date': Date,
    'Security Code': Code,
    'Security Name': SecName,
    'Client Name': Name,
    'Deal Type': Type,
    'Quantity': Quantity,
    'Price': Price,
})

df.to_excel('EXCELLL.xlsx', index=False)
