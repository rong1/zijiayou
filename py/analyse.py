#coding=utf-8

import re
import os
import lib
titlekey = ' <div class="maxtitle">(.*?)</div>' ;
#contentkey = '<div class="w740">(.*?)<!--end conright-->' ;
contentkey = '<div class="w740">(.*?)<!-----------赏start----------->' ;

def pureContent(s):
	content = s;

	#去掉 div span p等html元素
	patterns = ['<div(.*?)>','<span(.*?)>','<p(.*?)>','<ul(.*?)>','<li(.*?)>','<b(.*?)>','</(.*?)>','<a(.*?)>'];
	for pt in patterns :
		content = re.sub(pt,'%',content); #用%，方便正则查找

	#提取img
	imgpatterns = ['<img(.*?)src9="','" data-type(.*?)/>','<img(.*?)src="'];
	for pt in imgpatterns :
		content = re.sub(pt,'',content);
	content = re.sub('(%+)','\n',content);#去掉多个换行符
	lib.log(content);



#读取文件内容
furl = os.path.abspath('.')+"/input/threadowner-o-200099-69383635-1.html#pvareaid=101435.txt";

rfile = open(furl);
filecontent = rfile.read();
titles = re.findall(titlekey,filecontent);
if len(titles) == 1:
	lib.log(titles[0]);
contents = re.findall(contentkey,filecontent,re.S);
pureContent(contents[0]);

