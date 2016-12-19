# coding: utf-8

import leancloud
from get_toutiao_news import get_news
import constant.leancloud
import constant.toutiao as toutiao


def leancloud_init():
    leancloud.init(constant.leancloud.APP_ID, constant.leancloud.APP_KEY)


def create_toutiao(url, table_name):
    news_list = get_news(url)       # 获得头条新闻列表
    Table = leancloud.Object.extend(table_name)     # 创建表
    item_list = []
    for news in news_list:
        table = Table()
        table.set('image1', news.get_image1().decode("GBK"))
        table.set('image2', news.get_image2().decode("GBK"))
        table.set('image3', news.get_image3().decode("GBK"))
        table.set('title', news.get_title().decode("GBK"))
        table.set('source', news.get_source().decode("GBK"))
        table.set('link', news.get_link().decode("GBK"))
        item_list.append(table)
    Table.save_all(item_list)


if __name__ == "__main__":
    leancloud_init()
    create_toutiao(toutiao.URL_HOT, 'Hot')
    create_toutiao(toutiao.URL_SOCIETY, 'Society')
    create_toutiao(toutiao.URL_SPORTS, 'Sports')
    create_toutiao(toutiao.URL_ENTERTAINMENT, 'Entertainment')
    create_toutiao(toutiao.URL_WORLD, 'World')
    create_toutiao(toutiao.URL_FINANCE, 'Finance')
