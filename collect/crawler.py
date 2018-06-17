import os
import json
from datetime import datetime, timedelta
# from .api import api
from analysis_fb.collect.api import api

RESULT_DIRECTORY = '__results__/crawling'

def preprocess_post(post):
    # 공유수
    if 'shares' not in post:    # shares 가 post에 포함되어 있는거 아니지? 그렇다면:
        post['count_shares'] = 0
    else:    # shares 가 post에 포함되어 있다면:
        post['count_shares'] = post['shares']['count']

    # 전체 리액션 수
    if 'reactions' not in post:
        post['count_reactions'] = 0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']

    # 전체 코멘트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']

    # KST = UTC + 9
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=+9)
    # post['created_time'] = kst.strptime('%Y-%m-%d %H:%M:%S')
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')

def crawling(pagename, since, until):
    results = []
    filename = '%s/fb_%s_%s_%s.json' % (RESULT_DIRECTORY, pagename, since, until)

    for posts in api.fb_fetch_posts(pagename, since, until):
        for post in posts:
            preprocess_post(post)

        results += posts

    # save results to file(저장, 적재)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        print("json_string: " + json_string)
        outfile.write(json_string)
    #
    # if fetch:
    #     for posts in api.fb_fetch_posts(pagename, since, until):
    #         for post in posts:
    #             preprocess_post(post)
    #
    #         results += posts
    #
    #     # save results to file(저장, 적재)
    #     with open(filename, 'w', encoding='utf-8') as outfile:
    #         json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
    #         print("json_string: " + json_string)
    #         outfile.write(json_string)
    #
    return filename


if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)