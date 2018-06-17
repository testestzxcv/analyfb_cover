import sys
from urllib.request import Request, urlopen
from datetime import *
import json
try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'

    resp = urlopen(Request(url))
    resp_body = resp.read().decode('utf-8')
    json_result = json.loads(resp_body)

    print(json_result)
except Exception as e:
    print('%s %s' % (e, datetime.now()), file=sys.stderr)