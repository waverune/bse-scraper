import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict

URL = 'https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
FIELDS = ['Deal Date', 'Security Code', 'Security Name', 'Client Name', 'Deal Type', 'Quantity', 'Price']

# Function to get TD tags from url and headers
def get_td_tags(url, headers):
    html_data = requests.get(url, headers=headers)
    return BeautifulSoup(html_data.content).find_all('td', class_=['tdcolumn', 'tdcolumn text-right', 'TTRow_left'])

# Function to create dictionary of lists based on TD data
def get_list_data(td_tags, *args):
    args = args[0]
    lists = defaultdict(list)
    for index, info in enumerate(td_tags):
        lists[args[index % 7]].append(info.text)
    return lists

# Convert list data to pandas dataframe and generate excel
def generate_excel(lists):
    df = pd.DataFrame(lists)
    df.to_excel('EXCEL.xlsx', index=False)

# Main function
def main():
    td_tags = get_td_tags(URL, HEADERS)
    lists = get_list_data(td_tags, FIELDS)
    generate_excel(lists)

if __name__ == '__main__':
    main()
