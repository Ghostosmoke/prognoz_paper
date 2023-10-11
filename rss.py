import requests
import random
import pymorphy2
from itertools import groupby
from bs4 import BeautifulSoup
from user_aggents import user_agent_list
from category import category
from seek_list import seek_list
def random_user_agent_headers():
    '''Возвращет рандомный user-agent и друге параметры для имитации запроса из браузера'''
    rnd_index = random.randint(0, len(user_agent_list) - 1)
    return user_agent_list[rnd_index]
headers={
    'Accept':'* / *',
    "User-Agent":random_user_agent_headers()
}
def parsing_ria(http,seek_list):
    src=requests.get(http,headers=headers).text

    soup=BeautifulSoup(src,'lxml')



    now_site = BeautifulSoup(requests.get(http, headers=headers).text, 'lxml')
    last_news=now_site.find_all(category['ria']['text']['box'],class_='color-font-hover-only')


    for i in last_news:
        text=i.text
        for j in text.split():
            for seek in seek_list:
                if seek in j:
                    all_needs_news.append(morph.normal_forms(text)[0])
                    all_needs_news.append(category['ria']['link']+i.get('href'))
                    print(all_needs_news)
            # text[i]=morph.normal_forms(text[i])[0]


all_needs_news=[]
morph=pymorphy2.MorphAnalyzer(lang='ru')

print(morph.normal_forms('сТали стали стали')[0])
for name in category['ria']['http'].items():
    parsing_ria(name[1],seek_list)
