#coding=utf-8

import re
import os
import lib
titlekey = ' <div class="maxtitle">(.*?)</div>' ;
contentkey = '<div class="w740">(.*?)<!--end conright-->' ;
rcontentkey = '(.*?)<!-----------赏start----------->' ;



#处理NCR 组合方法
def _callback(matches):
    _id = matches.group(1);
    lib.log('unichr-------'+_id);

    try:
        return unichr(int(_id,16));
    except:
        lib.log('err');
        return _id

def decode_unicode_references(data):
    lib.log('ncr ====================');
    return re.sub("(&#x(.*?);)", _callback, data);


#净化内容
def pureContent(s):
	content = (re.findall(rcontentkey,s))[0];

	#去掉 div span p等html元素
	patterns = ['<div(.*?)>','<span(.*?)>','<p(.*?)>','<ul(.*?)>','<li(.*?)>','<b(.*?)>','</(.*?)>','<a(.*?)>'];
	for pt in patterns :
		content = re.sub(pt,'%',content); #用%，方便正则查找

	#提取img
	imgpatterns = ['<img(.*?)src9="','" data-type(.*?)/>','<img(.*?)src="'];
	for pt in imgpatterns :
		content = re.sub(pt,'',content);
	content = re.sub('(%+)','\n',content);#去掉多个换行符
	#处理NCR
	''' #JS 处理方法
	var regex_num_set = /&#(\d+);/g;
	var str = "Here is some text: &#27599;&#26085;&#19968;&#33394;|&#34013;&#30333;~"

	str = str.replace(regex_num_set, function(_, $1) {
	  return String.fromCharCode($1);
	});
	'''
	content = decode_unicode_references(content);

	lib.log(content);



#读取文件内容
furl = os.path.abspath('.')+"/input/threadowner-o-200099-69383635-1.html#pvareaid=101435.txt";

rfile = open(furl);
filecontent = rfile.read();
titles = re.findall(titlekey,filecontent);
if len(titles) == 1:
	lib.log(titles[0]);
contents = re.findall(contentkey,filecontent,re.S);
lib.log(len(contents));
lib.log(contents[1]);
pureContent(contents[1]);



