#coding=utf-8
import sys  #读命令行参数
import urllib  #读URL内容
import re  #正则
import binascii   #十六进制转字符串
import gzip,StringIO

titlekey = ' <div class="maxtitle">(.*?)</div>';
contentkey = '<div class="w740">(.*?)<!--end conright-->';
def getHtml(url_):
    page = urllib.urlopen(url_);
    html = page.read();
    return html;
def catchContent(url_):
    page = urllib.urlopen(url_);
    html = page.read();
    #print 'aa'+html;
    #html.decode('gb2312').encode('utf-8'); #以2312解码，再以utf-8编码来展示
    # 乱码是因为传输过程中用了gzip压缩，所以要用gzip解压后，再解码 参考文章 http://blog.csdn.net/ws491360104/article/details/50534863
    html = gzip.GzipFile(fileobj=StringIO.StringIO(html), mode="r");
    htmlR = html.read().decode('gb2312').encode('utf-8');
    #print 'bb'+html;
    title = re.findall(titlekey,htmlR)[0];
    #print "标题是："+title;
    content = re.findall(contentkey,htmlR,re.S);

    #print "内容是：" + content[0];
    content = content[0];
    #开始排除 html标签
    # 替换div
    divpattern = '<div(.*?)>';
    content = re.sub(divpattern,'',content);
    #print "去掉 div后内容是：" + content;
    spanpattern ='<span(.*?)>';
    content = re.sub(spanpattern,'',content);
    ppattern = '<p(.*?)>';
    content = re.sub(ppattern,'',content);

    patterns = ['<ul(.*?)>','<li(.*?)>','<b(.*?)>','</(.*?)>','<a(.*?)>'];

    for pt in patterns:
        content = re.sub(pt,'%',content); #用%，方便正则查找

    content = re.sub('(%+)','\n',content);#去掉多个换行符
    #print "去掉html标签后内容是：" + content;


    imgpatterns = ['<img(.*?)src9="','" data-type(.*?)/>','<img(.*?)src="'];



    for pt in imgpatterns:
        content = re.sub(pt,'',content);

    saveFile(content,title);
    #print "去掉img标签后内容是："+content;

    #content.replace('&nbsp','');
    #content.replace('//','http://'); #补全图片地址

    #print "补全图片地址后内容："  +content;
'''
    if len(content) == 0:
        print "没抓到内容";
    else :
        //saveHtmlFile(title,content[0]);
'''
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

'''    
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
'''

testurl = 'https://club.autohome.com.cn/bbs/thread-o-200099-70450049-1.html';
catchContent(testurl);

