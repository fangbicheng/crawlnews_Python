import time
import re
import csv

from selenium import webdriver
from bs4 import BeautifulSoup

import constant.toutiao as toutiao


def get_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, 10000)", "")
    time.sleep(10)
    page = driver.page_source
    driver.close()
    return page


def get_news(csv_file, url, category):
    # csvFile = open("crawlnews.csv", 'wb')
    writer = csv.writer(csv_file)

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

            writer.writerow(("", "", "", title, source, link, 0, category))
        if len(items[i].select('img')) == 1:
            print '1'
            image = items[i].select('img')[0].get('src')
            title = items[i].select('div[class="title-box"]')[0].get_text().strip().encode('GBK', 'ignore')
            link = link_head + items[i].select('div[class="title-box"]')[0].a['href'].strip()
            source = items[i].find_all('div', {"class": re.compile("lfooter$")})[0].find_all(
                '', {"class": re.compile("^((?!source).)+$")})[0].get_text().strip().encode('GBK', 'ignore')

            writer.writerow((image, "", "", title, source, link, 1, category))
        if len(items[i].select('img')) == 3:
            print '3'
            image1 = items[i].select('img')[0].get('src')
            image2 = items[i].select('img')[1].get('src')
            image3 = items[i].select('img')[2].get('src')
            title = items[i].select('div[class="title-box"]')[0].get_text().strip().encode('GBK', 'ignore')
            link = link_head + items[i].select('div[class="title-box"]')[0].a['href'].strip()
            source = items[i].find_all('div', {"class": re.compile("lfooter$")})[0].find_all(
                '', {"class": re.compile("^((?!source).)+$")})[0].get_text().strip().encode('GBK', 'ignore')

            writer.writerow((image1, image2, image3, title, source, link, 2, category))


if __name__ == "__main__":
    csvFile = open("crawlnews.csv", 'wb')
    get_news(csvFile, toutiao.URL_RECOMMEND, "recommend")
    get_news(csvFile, toutiao.URL_HOT, "hot")
    get_news(csvFile, toutiao.URL_SOCIETY, "society")
    get_news(csvFile, toutiao.URL_ENTERTAINMENT, "entertainment")
    get_news(csvFile, toutiao.URL_SPORTS, "sports")
    get_news(csvFile, toutiao.URL_FINANCE, "finance")
    get_news(csvFile, toutiao.URL_WORLD, "world")
    get_news(csvFile, toutiao.URL_MILITARY, "military")
    get_news(csvFile, toutiao.URL_TECH, "tech")
    get_news(csvFile, toutiao.URL_CAR, "car")
    get_news(csvFile, toutiao.URL_FUNNY, "funny")
    get_news(csvFile, toutiao.URL_FASHION, "fashion")
    get_news(csvFile, toutiao.URL_TRAVEL, "travel")
