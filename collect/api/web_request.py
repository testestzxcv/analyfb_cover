import json
from _datetime import *
from urllib.request import Request, urlopen
import sys

def html_request(
        url='',
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)     # request 객체 생성
        resp = urlopen(request)     # URL에 연결하여 response 객체 반환
        html = resp.read().decode(encoding)

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False: # 호출가능한 함수이면 True // is False -> 호출가능한 함수가 아니면
            return html # html을 리턴

        success(html)

    except Exception as e:
        if callable(error) is True: # error이 호출가능한 함수이면
            error(e) # error 함수 호출


def json_request(
        url='',
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)  # 리퀘스트 객체 생성
        resp = urlopen(request) # Url에 연결하여 response 객체 반환
        resp_body = resp.read().decode(encoding)   # 연결된 url에서 데이터를 읽어서 response body에 저장

        json_result = json.loads(resp_body) # 파이썬 형식으로 변환

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)


    except Exception as e:
        if callable(error) is True:
            error(e)
