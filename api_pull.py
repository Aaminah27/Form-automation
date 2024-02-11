from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json,pandas as pd
import os
from time import sleep

def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'15',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    pd.set_option('display.max_columns',None)
    #to make the data pretty
    df = pd.json_normalize(data['data'])
    #to store the time script is run in a column
    df['timestamp'] = pd.Timestamp.now()

    if not os.path.isfile(r'D:\Self_learning\practice_projects\output\api.csv'):
        df.to_csv(r'D:\Self_learning\practice_projects\output\api.csv', header = 'column_names')
    else:
        df.to_csv(r'D:\Self_learning\practice_projects\output\api.csv',mode='a',header=False)

for i in range(10):
    api_runner()
    print('API RUN Number ' + str(i))
    sleep(60)
exit()


#for manipulation with df and visualization : 
#https://colab.research.google.com/drive/1Ct42u3Uf3JZrkoxdGCsx4ROaC24lDba4#scrollTo=4ojUgBlfKkHV