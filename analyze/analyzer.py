import json
import re
from konlpy.tag import Twitter
from collections import Counter



# [a-zA-Z1-9]+ 정규표현식 알파벳 숫자 문자표현
# .* 모든문자열 표현
# [^\w] 공배 표현

def json_to_str(filename, key): # item['resultfile'] 'message' 전달
    jsonfile = open(filename, 'r', encoding='utf-8')    # crawling 에 저장된 파일 open
    json_string = jsonfile.read()   # crawling 에 저장된 파일 읽어서 json_string 에 저장
    jsonfile.close()

    data = ''
    json_data = json.loads(json_string) # 파일에서 읽은 데이터를 json 형식으로 변수에 저장
    for item in json_data:  # 파일에 있는 항목 하나씩 돌면서 불러온다
        value = item.get(key)   # 파일에 있는 항목에서 key(message) 값만 추출해서 변수에 저장
        if value is None:   # 변수에 내용이 없으면 continue
            continue

        data += re.sub(r'[^\w]', '', value) # value의 내용중에 지정한 문자를 제거한후 data변수에 저장

    return data # 저장된 문자열 전체 반환



def count_wordfreq(data):   # 형태소 분석 함수
    twitter = Twitter()
    nouns = twitter.nouns(data) # data에서 명사만 추출하여 변수에 저장

    count = Counter(nouns)  # 빈도수 계산을 위한 사전형태의 데이터 타입
    return count    # 빈도수 반환