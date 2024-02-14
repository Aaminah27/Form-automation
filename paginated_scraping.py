from bs4 import BeautifulSoup
import requests
import pandas as pd

columns = ['Item Title' , 'Price']
df= pd.DataFrame(columns = columns)
data = []
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
items = soup.find_all('div', class_='p-4')
count =1
for i in items:
    item_title = i.find('a').text
    item_price = i.find('h5')
    if item_price != None:
        item_price = item_price.text
        data =[item_title, item_price]
        length_df = len(df)
        df.loc[length_df] = data
        count = count +1
pages = soup.find('nav', class_='pagination')
urls=[]
links = pages.find_all('span',class_='page')
for link in links:
    a_tag = link.find('a')
 
    # Get the value of the href attribute
    if a_tag !=None:
        a_text = a_tag.text
        if a_text.isdigit():
            href_value = a_tag['href'] 
            # Extract the desired portion that is ?page=2
            text = href_value.split('/')[3]
            urls.append(text)

#loop through the list to scrape each page
for u in urls:
    #form a new url with previous base url and next page number
    new_url = url + u
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text,'lxml')
    items = soup.find_all('div', class_='p-4')
    #do the same thing as above to get title and price of products from each page
    for i in items:
        item_title = i.find('a').text
        item_price = i.find('h5')
        if item_price != None:
            item_price = item_price.text
            data =[item_title, item_price]
            length_df = len(df)
            df.loc[length_df] = data
            count = count +1
#lets export the df to a csv file
#set index to False os that it doesn't copy row numbering 
df.to_csv(r'products.csv', index=False)
