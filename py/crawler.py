#coding=utf-8
import sys  #读命令行参数
import urllib  #读URL内容
import re  #正则
import binascii   #十六进制转字符串

titlekey = "<title>(.*)</title>";
zhihuanwsercontentkey = '<div class="zm-editable-content clearfix">(.*?)</div>';
def getHtml(url_):
    page = urllib.urlopen(url_);
    html = page.read();
    return html;
def catchZhihu(url_):
    page = urllib.urlopen(url_);
    html = page.read();
    title = re.findall(titlekey,html)[0];
    content = re.findall(zhihuanwsercontentkey,html,re.S);
    print content;
    if len(content) == 0:
        print "没抓到内容";
    else :
        saveHtmlFile(title,content[0]);

def saveFile(content,title):
    f = open(title+".txt","wb");
    f.write(content);
    f.close();
def saveHtmlFile(title_,content_):
    header= '<head>        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> </head>';
    
    f = open(title_+".html","wb");
    f.write(header+content_);
    f.close();
def saveFileNoTitle(content_):
    title = extractTitle(content_)[0];
    saveFile(content_,title);

def extractTitle(html_):
    titlekey = "<title>(.*)</title>";
    title = re.findall(titlekey,html_);
    return title;
    
argslength = len(sys.argv); 
if argslength == 1:
    print "请输入要爬的地址/please tell us what you will check  ";
else :
    if argslength == 3:
        _url = sys.argv[1];
        _task = sys.argv[2];
    elif argslength == 2:
        _url = sys.argv[1];
        print "将为您展示/the content is \n    "
        text = getHtml(_url);
        print text


# text = getHtml("http://m.ddky.com/index.html");
text = getHtml("https://www.zhihu.com/question/51999936/answer/129171860");
str= extractTitle(text)[0];
# saveFileNoTitle(text);
catchZhihu("https://www.zhihu.com/question/51999936/answer/129171860");
# print str
# print text

