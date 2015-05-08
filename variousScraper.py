# -*- coding: utf-8-*-
import urllib2
from bs4 import BeautifulSoup
import os

def check_td_classes( css_class ) :
	if css_class in [ 'align_r', 'num2' ] :
		return True
	else :
		return False

dong_115 = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&rletNo=3678&hscpTypeCd=A01%3AA03%3AA04&bildNo=172770'
dong_117 = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&rletNo=3678&cortarNo=4146311800&hscpTypeCd=A01%3AA03%3AA04&mapX=127.1123034&mapY=37.3127311&mapLevel=12&page=&articlePage=&ptpNo=&rltrId=&mnex=&bildNo=314451&articleOrderCode=&cpId=&period=&prodTab=&atclNo=&atclRletTypeCd=&location=400&bbs_tp_cd=&sort=&siteOrderCode='
dong_112 = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&rletNo=3678&hscpTypeCd=A01%3AA03%3AA04&bildNo=576280'

dong_121 = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&rletNo=2880&cortarNo=4141010500&hscpTypeCd=A01%3AA03%3AA04&mapX=126.9371994&mapY=37.3598912&mapLevel=12&page=&articlePage=&ptpNo=&rltrId=&mnex=&bildNo=1182714&articleOrderCode=&cpId=&period=&prodTab=&atclNo=&atclRletTypeCd=&location=0&bbs_tp_cd=&sort=&siteOrderCode='
dong_122 = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&rletNo=2880&hscpTypeCd=A01%3AA03%3AA04&bildNo=1091513'
dong_124 = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=A1&rletNo=2880&cortarNo=4141010500&hscpTypeCd=A01%3AA03%3AA04&mapX=126.9371994&mapY=37.3598912&mapLevel=12&page=&articlePage=&ptpNo=&rltrId=&mnex=&bildNo=180410&articleOrderCode=&cpId=&period=&prodTab=&atclNo=&atclRletTypeCd=&location=0&bbs_tp_cd=&sort=&siteOrderCode='


def get_prices( dong_url_list ) :
	result_list = []

	for dong_url in dong_url_list :
		soup = BeautifulSoup( urllib2.urlopen( dong_url ), 'lxml' )
		result_tbody = soup.find( 'tbody' )
		trs = soup.find_all( 'tr' )

		for tr in trs :
			tds_loc = tr.find_all( 'td', class_ = check_td_classes )

			if len( tds_loc ) > 0 :
				dong = tds_loc[0].div.text
				cheung = tds_loc[1].div.span.text
				price = tds_loc[2].div.strong.text
				str = dong + ', ' + cheung + ', ' + price
				result_list.append( str )
			else :
				pass

	for result in result_list :
		print result

print u'죽전'
dong_url_list = [ dong_115, dong_117, dong_112 ]
get_prices( dong_url_list )

print u'산본'
dong_url_list = [ dong_121, dong_122, dong_124 ]
get_prices( dong_url_list )