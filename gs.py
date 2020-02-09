#!/usr/bin/env python
# encoding: utf-8
"""
@version: 
@author: xudong.wang
@file: 
@time: 
"""
import sys
from goose import Goose
from goose.text import StopWordsChinese
# url = 'https://baijiahao.baidu.com/s?id=1658026049992870938&wfr=spider&for=pc'
# g = Goose()
#
# article = g.extract(url=url)
# print u'标题:', article.title
# print u'描述:', article.meta_description
# print u'内容:', article.cleaned_text


def main(url):
    # url = 'https://baijiahao.baidu.com/s?id=1658026049992870938&wfr=spider&for=pc'
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    print u'标题:', article.title
    print u'描述:', article.meta_description
    print u'内容:', article.cleaned_text
    sys.exit()


if __name__ == '__main__':
    url = sys.argv[-1]
    print u'parse url:', url
    main(url)


