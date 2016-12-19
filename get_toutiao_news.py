import time
import re

from selenium import webdriver
from bs4 import BeautifulSoup

from bean.news import News


def get_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollBy(0, 5000)", "")
    time.sleep(3)
    page = driver.page_source
    driver.close()
    return page


def get_news(url):
    news_list = []
    link_head = 'http://toutiao.com'
    soup = BeautifulSoup(get_page(url))
    items = soup.find_all("div", {"class", "item-inner"})

    for i in range(0, len(items)):
        if len(items[i].select('img')) == 0:
            print '0'
            title = items[i].select('div[class="title-box"]')[0].get_text().strip().encode('GBK', 'ignore')
            link = link_head + items[i].select('div[class="title-box"]')[0].a['href'].strip()
            source = items[i].find_all('div', {"class": re.compile("lfooter$")})[0].find_all(
                '', {"class": re.compile("^((?!source).)+$")})[0].get_text().strip().encode('GBK', 'ignore')
            news = News('', '', '', title, source, link)
        if len(items[i].select('img')) == 1:
            print '1'
            image = items[i].select('img')[0].get('src')
            title = items[i].select('div[class="title-box"]')[0].get_text().strip().encode('GBK', 'ignore')
            link = link_head + items[i].select('div[class="title-box"]')[0].a['href'].strip()
            source = items[i].find_all('div', {"class": re.compile("lfooter$")})[0].find_all(
                '', {"class": re.compile("^((?!source).)+$")})[0].get_text().strip().encode('GBK', 'ignore')
            news = News(image, '', '', title, source, link)
        if len(items[i].select('img')) == 3:
            print '3'
            image1 = items[i].select('img')[0].get('src')
            image2 = items[i].select('img')[1].get('src')
            image3 = items[i].select('img')[2].get('src')
            title = items[i].select('div[class="title-box"]')[0].get_text().strip().encode('GBK', 'ignore')
            link = link_head + items[i].select('div[class="title-box"]')[0].a['href'].strip()
            source = items[i].find_all('div', {"class": re.compile("lfooter$")})[0].find_all(
                '', {"class": re.compile("^((?!source).)+$")})[0].get_text().strip().encode('GBK', 'ignore')
            news = News(image1, image2, image3, title, source, link)

        news_list.append(news)

    return news_list
