import collect

if __name__ == '__main__':
    items = [{'pagename': 'jtbcnews', 'since': '2017-01-01', 'until':'2017-12-31'}]

    # 데이터 수집(collection)
    for item in items:
        resultfile = collect.crawling(**item)
        item['resultfile'] = resultfile

    print(items)