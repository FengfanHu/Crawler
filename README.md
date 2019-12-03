# Dictionary Crawler
Python中英字典爬虫
> Packages
 - [Flask](https://github.com/pallets/flask)
 - [Bootstrap_flask](https://github.com/greyli/bootstrap-flask)
 - [Requests](https://github.com/psf/requests)
***

## BeautifulSoup

### Install
```python3
pip3 install requests
pip3 install beautifulsoup4
pip3 install html5lib   #用于解析 HTML5
```
### Usage
> 获取HTML内容
```python3
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
response = requests.get(search_url, headers=headers)
html_content = response.content
```
> Start BeautifulSoup
>> SoupStrainer is used to filiter main content
```python3
body = BeautifulSoup(html_content, 'html5lib')
# entry_body = BeautifulSoup(html_content, 'html', parse_only=SoupStrainer('div',\
#     attrs={"class":'entry-body'}))
body.findAll('TagName', attrs={'Attributes': 'Name'})
Tag.get_text() #获取标签内的文字
```
