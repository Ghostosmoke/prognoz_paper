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
def parsing_ria(name,http,seek_list):
    src=requests.get(http,headers=headers).text

    soup=BeautifulSoup(src,'lxml')

    page=soup.find_all('a',class_='pagination')
    #Проверка сколько страниц
    if page==[]:
        page.append(1)
    else:
        page[-1]=page[-1].text
    for i in range(int(page[-1])):
        if i==0:

            now_site = BeautifulSoup(requests.get(http, headers=headers).text, 'lxml')
            print(http)

        else:
            now_site = BeautifulSoup(requests.get(http+'/'+str(i), headers=headers).text, 'lxml')
            print(http+'/'+str(i))
        last_news=now_site.find_all(category['investing']['text']['box'],class_='title')


    for i in last_news:
        text=i.text
        for j in text.split():
            for seek in seek_list:
                if seek in j:
                    all_needs_news.append(morph.normal_forms(text)[0])
                    all_needs_news.append(category['investing']['link']+i.get('href'))
all_needs_news=[]
morph=pymorphy2.MorphAnalyzer(lang='ru')


for name in category['investing']['http'].items():
    parsing_ria(name[0],name[1],seek_list)
