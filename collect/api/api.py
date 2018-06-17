from urllib.parse import urlencode
from .web_request import json_request


ACCESS_TOKEN = 'EAACEdEose0cBAJ2K86ZC1ayVNY2DVdWVu6iqTwQZAdLLdpLZBp21dSMdrGp4IcZBzoqT1X6kBUuWvjDr1hBOLoC4zSuTcrOenryfZA9gowGqudKUOzoqBZBKZCeoCSDS7vMZBWyAaXxAHLPxXJmMG2aUkhE6xFbNeBeD4ZCzV7h0dKOG89j9Y5Kir33edFypHdIYm1qZCi6ZCYqnZAzUcFtzWWSwbmqy0fMPy8MZD'
BASE_URL_FB_API = 'https://graph.facebook.com/v3.0'

def fb_gen_url(base=BASE_URL_FB_API, node='', **param):
    url = "%s/%s/?%s" % (base, node, urlencode(param))
    return url

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)  # 페이지 네임과 엑세스 토큰 포함한 url 주소를 저장
    json_result = json_request(url=url)
    return json_result.get("id")

def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(node=fb_name_to_id(pagename)+"/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since,
                     until=until,
                     limit=50,
                     access_token=ACCESS_TOKEN)
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging') # json_result 가 None이면 paging에 None을 넣고, 있으면 json_result에서 paging 부분을 가져온다
        posts = None if json_result is None else json_result.get('data')

        url = None if paging is None else paging.get("next")

        isnext = url is not None

        yield posts
