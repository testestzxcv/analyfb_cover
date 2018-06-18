import pytagcloud
import os
import collections
import matplotlib.pyplot as plt

RESULT_DIRECTORY = "__results__/visualization"

def wordcloud(filename, wordfreq):
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)    # 상위 빈도수 dict을 이용하여 태크를 만듬
    print("taglist === " ,taglist)
    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)    # 태그 파일명

    pytagcloud.create_tag_image(
        taglist,    # 태그 리스트
        save_filename,  # 파일명
        size=(900, 600),    # 캔버스 사이즈
        fontname='Malgun',  # 폰트
        rectangular=False,  # 사각형 여부
        background=(0, 0, 0))

def graph_bar(title=None, xlabel=None, ylabel=None, showgrid=False, values=None, ticks=None, filename=None, showgraph=True):
    fig, subplots = plt.subplots(1, 1)
    subplots.bar(range(len(values)), values, align='center')

    plt.show()


#
# if os.path.exists(RESULT_DIRECTORY) is False:
#     os.mkdir(RESULT_DIRECTORY)