# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import requests
import re
import json

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
    "cookie": r"_ntes_nnid=d210a1ed73ac8d49791dd9e007b8a7e7,1634192367969; _ntes_nuid=d210a1ed73ac8d49791dd9e007b8a7e7; UM_distinctid=17fbfa77430187-0d1d26d2b671fc-5617185b-100200-17fbfa77431f41; vinfo_n_f_l_n3=3cc07e6b80b1c971.1.0.1648187892685.0.1648187967384; EDUWEBDEVICE=398a0755db534b7f8b428017d18913a2; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; sideBarPost=1970; xuetangvendor=ykt_store_xiaomi; keoutvendor=; ke_Pdt=ydkWeb; ke_inLoc=; OUTFOX_SEARCH_USER_ID_NCOO=1288925762.7441041; hb_MA-BFF5-63705950A31C_source=study.163.com; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1655949225,1655953652,1656002346,1656210125; courseId=59009; NTESSTUDYSI=84da42124bda4da3b4f26065cef03eed; NTES_YD_SESS=ueeMVO1OF1gMbOUnwrzr41LJcEIKEVtD5L47G_bRG90QZ2qhZLps8Njp3imEQpNGZIs_QgT4slAQmmQOgwNM_jgiBYJms.NqAP7oInEuyLqEB_AzCa0uaL..vG0AVPv6okQuucbbvxRpNu75LIdPiAW0d3dT6T7j2th3pyg6vNiPqGQj9TaAPZS5yXARganVTdvx.ACWOMxT8unsd5bKi_gsFGEJ9n6HMVXXZ5SVA4Moi; NTES_YD_PASSPORT=1MO6bF40jEdNWQmQ2SrNYG.BnXt1obLPnVlWa0Jp.NnlceKDcQzbiWZz7LqFIzWscvbNIuHnb9RDQK9sLCGpRVd.7o51FRZ7XFbDBOFGCrKDL9LIabrmqyO.KoVrMukkvgldIL97L8WolUSEVMb91EuNp6w9vqfnN_MyUUt.vzDy2xwScGHR18UfD5xbPtuR8W0r2kYL9xiATUg8xmzT9A5Hx; S_INFO=1656223239|0|0&60##|13828460875; P_INFO=13828460875|1656223239|1|study|00&99|null&null&null#gud&440100#10#0#0|&0|null|13828460875; DICT_SESS=v2|7mHe6giZ2RYA0fkA0MQS0zWOLqFhfqy0JyRMkYhMg40gF0fJKhfpZ0zG0HJSOMg40PLO4kfkM6L0gu0fzM64wu0OEnfUfhM6F0; DICT_LOGIN=1||1656223239680; NETEASE_WDA_UID=1453061710#|#1611456020195; NTES_STUDY_YUNXIN_ACCID=s-1453061710; NTES_STUDY_YUNXIN_TOKEN=09261a82a7d73dbe17ce8b7aa6377359; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9rZS5zdHVkeS4xNjMuY29tL2NvdXJzZS9kZXRhaWwvNTkwMDk/UGR0PXlka1dlYg==; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1656226243; lessonId=3040815; JSESSIONID=1712AF307A59A8DEB8C923A9EDFED407"
}


# 杨亮讲英文·全民英语背诵营  https://ke.study.163.com/course/detail/59009
def getRecitationCamp(url=r'https://ke.study.163.com/course/detail/59009'):
    courseId = re.search(r'\d{5}$',url).group()
    # print(f'courseId = {courseId}')
    session = requests.session()
    resp = requests.get(url, headers=headers)
    # print(resp.text)

    obj = re.compile(r'window.lesson =(?P<lst>.*}])', re.S)
    tmp = obj.finditer(resp.text)
    for it in tmp:
        lst = it.group("lst")
    res = json.loads(lst)

    # res[0] :　新人必读
    # res[１] :　每日学习
    # res[２] :　每周精讲
    # print(type(res[1]))
    # print(res[1])
    # print(res[1]["id"])
    # print(res[1]["level"])
    # print(res[1]["list"])
    # print(res[1]["liveTime"])
    # print(res[1]["planNum"])
    # print(res[1]["title"])
    # print(res[1]["list"])
    # print(len(res[1]['list']))

    # print(res[1]["id"])
    for it in res[1]["list"][67:]: # 每日学习
        print("*****************************************************************************")
        # print(it)
        for i in it['list']:
            print("                     ****************************************************************")
            articleId = i.get('articleId')
            lessonId = i.get('id')
            title = i.get('title')
            # https://ke.study.163.com/topic/study/article/index.html?pid=42758&courseId=59009&lessonId=3040761
            url_lesson = f'https://ke.study.163.com/topic/study/article/index.html?pid={articleId}&courseId={courseId}&lessonId={lessonId}'
            url_article = f'https://ke.study.163.com/cms/api/{articleId}?noCache=true&api_version=2.1'
            # print(i)
            print(f'url_lesson is {url_lesson}')
            print(f'url-article is {url_article}')
            getSubSeries(url_article)


# refer "https://ke.study.163.com/topic/study/article/index.html?pid=16096&courseId=59009&lessonId=3040763#/"
def getSubSeries(url):  # url ='https://ke.study.163.com/cms/api/43175?noCache=true&api_version=2.1&callback=reqwest_1656220048521'
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    # print(resp.status_code)
    # print(resp.headers)
    # print(resp.cookies)
    # print(resp.json())
    # print(type(resp.json()))

    # print(f'resp.content is {resp.content}')
    # print(f'type of resp.content is {type(resp.content)}')
    #
    # print(f'resp.text is {resp.text}')
    # print(f'type of resp.text is {type(resp.text)}')

    # handle exception case i.e  url ='https://ke.study.163.com/cms/api/None
    # if not resp.json():
    # if resp.status_code != '200':
    if not resp.json() or resp.json().get('success') is False:
        print(f'Not data returned from url {url}')
        return

    title = resp.json()["title"].replace('|', '').replace('?', '')
    print(f'get {title} data starting.......')

    obj = re.compile(r'[a-zA-z]+://[^\s]*mp4', re.S)
    obj2 = re.compile(r'[a-zA-z]+://[^\s]*mp3', re.S)

    url_mp4 = obj.findall(resp.text)
    url_mp3 = obj2.findall(resp.text)
    # print(url_mp4)
    # print(url_mp3)
    resp.close()

    # download
    i = 0
    for a in url_mp4:
        i = i + 1
        resp_mp4 = requests.get(a, headers=headers)
        file = f'{title}_{i}.mp4'
        print(f'{file} is downloading')
        with open(f"{title}_{i}.mp4", mode="wb") as f:
            f.write(resp_mp4.content)
            file = f'{title}_{i}.mp4'
            print(f'{file} saved')
        resp_mp4.close()

    i = 0
    for a in url_mp3:
        i = i + 1
        resp_mp3 = requests.get(a, headers=headers)
        file = f'{title}_{i}.mp3'
        print(f'{file} is downloading')
        with open(f"{title}_{i}.mp3", mode="wb") as f:
            f.write(resp_mp3.content)
            file = f'{title}_{i}.mp3'
            print(f'{file} saved')
        resp_mp3.close()
    print(f'get {title} data done.......')

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print_hi('PyCharm')
    # https://ke.study.163.com/cms/download/15852
    # GetSubSeries(r'https://ke.study.163.com/cms/api/16096')
    # getSubSeries(r'https://ke.study.163.com/cms/api/16096')
    getRecitationCamp()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
