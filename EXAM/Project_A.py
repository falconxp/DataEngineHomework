
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

df_head = ['model_series','lowest_price','highest_price','img_url']

def get_content(request_url):
    # 获取页面内容
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'}
    html = requests.get(request_url, headers=headers, timeout=10)
    content = html.text
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup


def content_analysis(soup):
    global df_head
    df = pd.DataFrame(columns=df_head)
    # 获得目标内容
    table = soup.find('div', class_='search-result-list')
    # 找到3组源数据出处
    name_list = table.find_all(class_='cx-name text-hover')
    price_list = table.find_all(class_='cx-price')
    img_list = table.find_all(class_='img')
    # 解析源数据，存入df
    for i in range(len(name_list)):
        item = {}
        item['model_series'] = name_list[i].text
        price = price_list[i].text
        if price == "暂无":
            item['lowest_price'] = np.NaN
            item['highest_price'] = np.NaN
        else:
            item['lowest_price'] = float(price.split('-')[0])
            item['highest_price'] = float(price.split('-')[1][:-1])
        item['img_url'] = str('http:') + img_list[i]['src']
        df = df.append(item,ignore_index = True)
    return df


def complaint_scrap():

    global df_head
    result = pd.DataFrame(columns=df_head)
    request_url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
    # 抓取每页内容
    soup = get_content(request_url)
    # 解析每页内容，结果添加在DataFrame最后
    df = content_analysis(soup)
    result = result.append(df, ignore_index=True)
    result.to_csv('bitauto_price_vw.csv', index=False, encoding='gbk')


def main():
    complaint_scrap()


if __name__ == "__main__":
    main()