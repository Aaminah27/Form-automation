from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://books.toscrape.com/'
page = requests.get(url)
# Specify the correct encoding to remove  A character in the price'Â£35.02'
html_content = page.content.decode('utf-8')  
soup = BeautifulSoup(html_content, 'html.parser')

get_ol= soup.find_all('ol')

columns_name = ['Title','Price', 'Availability','Link to Book']
#creating dataframe from above columns
df =pd.DataFrame(columns=columns_name)

#all the books are inside ol tag
for li in get_ol:
    #for each ol we need to get the li tag to get each book
    get_li = li.find_all('li')
    for article in get_li:
        #inside li there is an article tag which encompasses the books info
        get_article = article.find_all('article')
        for elements in get_article:
            #to get title and link
            get_h3 = elements.find_all('h3')
            #accessing price
            get_price_tag = elements.find('p', class_='price_color')
            price = get_price_tag.text
            #accessing stock avaliablity
            get_availablity = elements.find('p', class_='instock availability')
            #strip as there were spaces in it
            availablity = get_availablity.text.strip()
            for a_tag in get_h3:
                get_a = a_tag.find_all('a')
                for link_element in get_a:
                    title_attribute = link_element.get('title')
                    link_attribute = link_element.get('href')
                    #get the length of dataframe
                    lenght_df = len(df)
                    #insert each row as we get it into the dataframe
                    data = [title_attribute,price,availablity,url+link_attribute]
                    df.loc[lenght_df] = data

#lets export the df to a csv file
#set index to False os that it doesn't copy row numbering 
df.to_csv(r'path_to_csv_file', index=False, encoding='utf-8-sig')
