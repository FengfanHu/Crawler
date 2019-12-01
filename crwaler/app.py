from bs4 import BeautifulSoup, SoupStrainer
import requests, re
from .model import Camdic_model, Oxfdic_model

cam_url_prefix = "https://dictionary.cambridge.org/dictionary/english-chinese-simplified/"
oxf_url_prefix = "https://www.oxfordlearnersdictionaries.com/definition/english/"
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

'''
Crwaler for Cambridge Dictionary:
Input:      key_word(string)
Output:     obj_array(list)

SoupStrainer is used to filiter main content
however html5 doesn't support parse_only
'''
def cam_crwaler(key_word):
    search_url = cam_url_prefix+key_word
    response = requests.get(search_url, headers=headers)
    html_content = response.content
    body = BeautifulSoup(html_content, 'html5lib')
    # entry_body = BeautifulSoup(html_content, 'html', parse_only=SoupStrainer('div',\
    #     attrs={"class":'entry-body'}))
    parts = body.findAll('div', attrs={'class': 'pr entry-body__el'})
    items = body.findAll('div', attrs={'class': "lmb-12"})
    obj_array = []
    item_array = []
    for part in parts:
        #Header
        title = part.find('span', attrs={'class': "hw dhw"})
        label = part.find('span', attrs={'class': "pos dpos"})
        uk_audio = part.find('span', attrs={'class': "uk dpron-i"})
        audio_src = uk_audio.contents[1].contents[1].contents[3]['src']
        audio_symbol = uk_audio.find('span', attrs={'class': "pron dpron"})
        rank = part.find('span', attrs={'class': re.compile("^epp-xref")})
        #Content
        define = part.find('div', attrs={'class': "def ddef_d db"})
        trans = part.find('span', attrs={'class': "trans dtrans dtrans-se"})
        examples = part.findAll('div', attrs={'class': "examp dexamp"})
        camdic_obj = Camdic_model(title, label, audio_src, audio_symbol, rank, define, trans, examples)
        obj_array.append(camdic_obj)
    for item in items:
        link = item.find('a')
        item_array.append(link)
    return obj_array, item_array

def oxf_crwaler(key_word):
    search_url = oxf_url_prefix+key_word+"_1"
    response = requests.get(search_url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html5lib')
    body = soup.find('div', attrs={'class':"entry"})
    head = body.find('div', attrs={'class':"top-container"})
    parts = body.findAll('li', attrs={'class':"sn-g"})
    #Header
    title = body.find('h2', attrs={'class':"h"})
    label = head.find('span', attrs={'class':"pos"})
    audio = head.find('span', attrs={'class':"pron-g"})
    audio_symbol = audio.find('span', attrs={'class':'phon'})
    audio_src = audio.find('div', attrs={'class': re.compile("^sound")})['data-src-mp3']
    #Content
    contents = []
    for part in parts:
        sub_title = part.find('strong')
        define = part.find('span', attrs={'class':"def"})
        examples = part.findAll('span', attrs={'class':'x'})
        contents.append((sub_title, define, examples))
    ofx_obj = Oxfdic_model(title, label, audio_src, audio_symbol, contents)
    #Near By
    browses = soup.find('div', attrs={'class':"responsive_row nearby"})
    browse = browses.findAll('data', attrs={'class':"hwd"})
    return ofx_obj, browse

if __name__ == "__main__":
    # parts = cam_crwaler("content")
    # print(type(parts), len(parts))
    # print(parts[0].title)
    # print(parts[0].label)
    # print(parts[0].audio_src)
    # print(parts[0].audio_symbol)
    # print(parts[0].rank)
    # print(parts[0].define)
    # print(parts[0].trans)
    # print(parts[0].examples)
    # print(parts[0].browse)

    # oxf_crwaler('content')
    pass
