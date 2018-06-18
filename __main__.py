import collect
import analyze
import visualize

if __name__ == '__main__':
    items = [{'pagename':'jtbcnews', 'since':'2018-01-01', 'until':'2018-12-31'},
             {'pagename':'chosun', 'since':'2018-01-01', 'until':'2018-12-31'}]

    # # 데이터 수집(collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile


    # 데이터 분석(analyze)
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)   # 명사만 추출하여 items 사전에 추가
        print(item['count_wordfreq'])    # 빈도수 출력

    # 데이터 시각화(visualize)
    for item in items:
        count = item['count_wordfreq']  # dict 형식으로 빈도수 출력
        count_m50 = dict(count.most_common(50)) # 높은 빈도수 순서대로 지정값 갯수만큼 출력

        filename = "%s_%s_%s" % (item['pagename'], item['since'], item['until'])
        visualize.wordcloud(filename, count_m50)
