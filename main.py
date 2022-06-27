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
def getRecitationCamp(url):
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


# 杨亮讲英文·全民英语背诵营  https://ke.study.163.com/course/detail/59009
# 每周精讲
def getRecitationCamp2(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
        "cookie": "_ntes_nnid=d210a1ed73ac8d49791dd9e007b8a7e7,1634192367969; _ntes_nuid=d210a1ed73ac8d49791dd9e007b8a7e7; UM_distinctid=17fbfa77430187-0d1d26d2b671fc-5617185b-100200-17fbfa77431f41; vinfo_n_f_l_n3=3cc07e6b80b1c971.1.0.1648187892685.0.1648187967384; EDUWEBDEVICE=398a0755db534b7f8b428017d18913a2; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; sideBarPost=1970; xuetangvendor=ykt_store_xiaomi; keoutvendor=; ke_Pdt=ydkWeb; ke_inLoc=; OUTFOX_SEARCH_USER_ID_NCOO=1288925762.7441041; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1655949225,1655953652,1656002346,1656210125; courseId=59009; NTESSTUDYSI=84da42124bda4da3b4f26065cef03eed; NTES_YD_SESS=ueeMVO1OF1gMbOUnwrzr41LJcEIKEVtD5L47G_bRG90QZ2qhZLps8Njp3imEQpNGZIs_QgT4slAQmmQOgwNM_jgiBYJms.NqAP7oInEuyLqEB_AzCa0uaL..vG0AVPv6okQuucbbvxRpNu75LIdPiAW0d3dT6T7j2th3pyg6vNiPqGQj9TaAPZS5yXARganVTdvx.ACWOMxT8unsd5bKi_gsFGEJ9n6HMVXXZ5SVA4Moi; NTES_YD_PASSPORT=1MO6bF40jEdNWQmQ2SrNYG.BnXt1obLPnVlWa0Jp.NnlceKDcQzbiWZz7LqFIzWscvbNIuHnb9RDQK9sLCGpRVd.7o51FRZ7XFbDBOFGCrKDL9LIabrmqyO.KoVrMukkvgldIL97L8WolUSEVMb91EuNp6w9vqfnN_MyUUt.vzDy2xwScGHR18UfD5xbPtuR8W0r2kYL9xiATUg8xmzT9A5Hx; S_INFO=1656223239|0|0&60##|13828460875; P_INFO=13828460875|1656223239|1|study|00&99|null&null&null#gud&440100#10#0#0|&0|null|13828460875; DICT_SESS=v2|7mHe6giZ2RYA0fkA0MQS0zWOLqFhfqy0JyRMkYhMg40gF0fJKhfpZ0zG0HJSOMg40PLO4kfkM6L0gu0fzM64wu0OEnfUfhM6F0; DICT_LOGIN=1||1656223239680; NETEASE_WDA_UID=1453061710#|#1611456020195; NTES_STUDY_YUNXIN_ACCID=s-1453061710; NTES_STUDY_YUNXIN_TOKEN=09261a82a7d73dbe17ce8b7aa6377359; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1656226243; lessonId=3040823; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9saXZlLnN0dWR5LjE2My5jb20v; hb_MA-BFF5-63705950A31C_source=ke.study.163.com; JSESSIONID=D5E3A3CA224EE61860EE2DDC18B17F1B_ntes_nnid=d210a1ed73ac8d49791dd9e007b8a7e7,1634192367969; _ntes_nuid=d210a1ed73ac8d49791dd9e007b8a7e7; UM_distinctid=17fbfa77430187-0d1d26d2b671fc-5617185b-100200-17fbfa77431f41; vinfo_n_f_l_n3=3cc07e6b80b1c971.1.0.1648187892685.0.1648187967384; EDUWEBDEVICE=398a0755db534b7f8b428017d18913a2; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; sideBarPost=1970; xuetangvendor=ykt_store_xiaomi; keoutvendor=; ke_Pdt=ydkWeb; ke_inLoc=; OUTFOX_SEARCH_USER_ID_NCOO=1288925762.7441041; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1655949225,1655953652,1656002346,1656210125; courseId=59009; NTESSTUDYSI=84da42124bda4da3b4f26065cef03eed; NTES_YD_SESS=ueeMVO1OF1gMbOUnwrzr41LJcEIKEVtD5L47G_bRG90QZ2qhZLps8Njp3imEQpNGZIs_QgT4slAQmmQOgwNM_jgiBYJms.NqAP7oInEuyLqEB_AzCa0uaL..vG0AVPv6okQuucbbvxRpNu75LIdPiAW0d3dT6T7j2th3pyg6vNiPqGQj9TaAPZS5yXARganVTdvx.ACWOMxT8unsd5bKi_gsFGEJ9n6HMVXXZ5SVA4Moi; NTES_YD_PASSPORT=1MO6bF40jEdNWQmQ2SrNYG.BnXt1obLPnVlWa0Jp.NnlceKDcQzbiWZz7LqFIzWscvbNIuHnb9RDQK9sLCGpRVd.7o51FRZ7XFbDBOFGCrKDL9LIabrmqyO.KoVrMukkvgldIL97L8WolUSEVMb91EuNp6w9vqfnN_MyUUt.vzDy2xwScGHR18UfD5xbPtuR8W0r2kYL9xiATUg8xmzT9A5Hx; S_INFO=1656223239|0|0&60##|13828460875; P_INFO=13828460875|1656223239|1|study|00&99|null&null&null#gud&440100#10#0#0|&0|null|13828460875; STUDY_INFO=\"yd.a3d7bb5d90db452b8@163.com|8|1453061710|1656223239623\"; STUDY_SESS=\"ewwZXGPJCgIdhQZyKlAivbZNqDfdcnEYZC/3PYNvIPK7ARHbjp0KbtBiBQalOelEd576j8fTOQCEVtBIlPoDXu2pTrhCv5qJw3FR+Pg79GeqbpjAueOJbD6+pMWWg6FTf9G1iKzelXZAsBruHkqPQ5R71g5qdVzGq5waCm7Zl7sLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA==\"; STUDY_PERSIST=\"kR1jDZcxnohSw5v8UKhRctaBEHFrHRM0wpAW6CZRNp3Us6MLk+u/5dDs7I7+wuwLRYyCfO7dmeYkYH9evgZ+TVGaQ6FMiwp7siATddSBWseef6+fMAN5DhLjINSp2lSGmUveXmppQUzPFmneDOsmwxUKiT+YMPwCR6WxpJJRyw+8yQ70F+ClzJS/yIxAnlsIWem4V0ikHFr/EI1uZ/2fNWLXTpQdnuvatQT8FbzNggDZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU=\"; DICT_SESS=v2|7mHe6giZ2RYA0fkA0MQS0zWOLqFhfqy0JyRMkYhMg40gF0fJKhfpZ0zG0HJSOMg40PLO4kfkM6L0gu0fzM64wu0OEnfUfhM6F0; DICT_LOGIN=1||1656223239680; NETEASE_WDA_UID=1453061710#|#1611456020195; NTES_STUDY_YUNXIN_ACCID=s-1453061710; NTES_STUDY_YUNXIN_TOKEN=09261a82a7d73dbe17ce8b7aa6377359; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1656226243; lessonId=3040823; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9saXZlLnN0dWR5LjE2My5jb20v; hb_MA-BFF5-63705950A31C_source=ke.study.163.com; JSESSIONID=1CE0D018CFC8F275E7C367960D71615F"
    }
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

    # print(res[2])
    for it in res[2]["list"]: # 每周精讲
        print("*****************************************************************************")
        # print(type(it))
        print(it)
        lessonid = it.get('id')
        # typeid = it.get('type')
        title = it.get('title')

        if it.get('material'):
            # download the PDF file
            url_pdf = it.get('material')
            resp_pdf = requests.get(url_pdf,headers=headers)
            file = f'{title}.pdf'
            print(f'{file} is downloading')
            with open(f"{file}", mode="wb") as f:
                f.write(resp_pdf.content)
            print(f'{file} saved')
            continue

        if it.get('video'):
            # format the url and download it directly
            # https://live.study.163.com/live/index.html?courseId=59009&lesson=3040821&type=1
            # the url of video  https://ke.study.163.com/course/video.json?lessonId=3040821
            url_video = f'https://ke.study.163.com/course/video.json?lessonId={lessonid}'
            print(url_video)
            resp_video = requests.get(url_video, headers=headers)
            resp_video.encoding = resp_video.apparent_encoding
            # print(resp_video.text)

            if not resp_video.json() or resp_video.json().get('success') is False:
                print(f'Not data returned from url {url_video}')
                continue

            url_mp4 = resp_video.json().get('result').get('videoUrl')
            lessonTitle = resp_video.json().get('result').get('lessonTitle')
            print(f'get {lessonTitle} video data starting.......')
            resp_video.close()

            # download
            resp_mp4 = requests.get(url_mp4, headers=headers)
            with open(f"{lessonTitle}.mp4", mode="wb") as f:
                f.write(resp_mp4.content)
            print(f'{lessonTitle}.mp4 saved')
            resp_mp4.close()
            continue

        if it.get('url'):
            # https://ke.study.163.com/cms/api/42299?noCache=true&api_version=2.1
            articleId = it.get('articleId')
            # https://ke.study.163.com/topic/study/article/index.html?pid=42758&courseId=59009&lessonId=3040761
            url_article = f'https://ke.study.163.com/cms/api/{articleId}?noCache=true&api_version=2.1'
            print(f'url-article is {url_article}')
            getSubSeries(url_article)
            continue


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
        print(f'{file} saved')
        resp_mp3.close()
    print(f'get {title} data done.......')

def getwords(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
        "cookie": "___rl__test__cookies=1656247502855; _ntes_nnid=d210a1ed73ac8d49791dd9e007b8a7e7,1634192367969; _ntes_nuid=d210a1ed73ac8d49791dd9e007b8a7e7; UM_distinctid=17fbfa77430187-0d1d26d2b671fc-5617185b-100200-17fbfa77431f41; vinfo_n_f_l_n3=3cc07e6b80b1c971.1.0.1648187892685.0.1648187967384; EDUWEBDEVICE=398a0755db534b7f8b428017d18913a2; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; sideBarPost=1970; xuetangvendor=ykt_store_xiaomi; keoutvendor=; ke_Pdt=ydkWeb; ke_inLoc=; OUTFOX_SEARCH_USER_ID_NCOO=1288925762.7441041; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1655949225,1655953652,1656002346,1656210125; NTESSTUDYSI=84da42124bda4da3b4f26065cef03eed; NTES_YD_SESS=ueeMVO1OF1gMbOUnwrzr41LJcEIKEVtD5L47G_bRG90QZ2qhZLps8Njp3imEQpNGZIs_QgT4slAQmmQOgwNM_jgiBYJms.NqAP7oInEuyLqEB_AzCa0uaL..vG0AVPv6okQuucbbvxRpNu75LIdPiAW0d3dT6T7j2th3pyg6vNiPqGQj9TaAPZS5yXARganVTdvx.ACWOMxT8unsd5bKi_gsFGEJ9n6HMVXXZ5SVA4Moi; NTES_YD_PASSPORT=1MO6bF40jEdNWQmQ2SrNYG.BnXt1obLPnVlWa0Jp.NnlceKDcQzbiWZz7LqFIzWscvbNIuHnb9RDQK9sLCGpRVd.7o51FRZ7XFbDBOFGCrKDL9LIabrmqyO.KoVrMukkvgldIL97L8WolUSEVMb91EuNp6w9vqfnN_MyUUt.vzDy2xwScGHR18UfD5xbPtuR8W0r2kYL9xiATUg8xmzT9A5Hx; S_INFO=1656223239|0|0&60##|13828460875; P_INFO=13828460875|1656223239|1|study|00&99|null&null&null#gud&440100#10#0#0|&0|null|13828460875; STUDY_INFO=\"yd.a3d7bb5d90db452b8@163.com|8|1453061710|1656223239623\"; STUDY_SESS=\ewwZXGPJCgIdhQZyKlAivbZNqDfdcnEYZC/3PYNvIPK7ARHbjp0KbtBiBQalOelEd576j8fTOQCEVtBIlPoDXu2pTrhCv5qJw3FR+Pg79GeqbpjAueOJbD6+pMWWg6FTf9G1iKzelXZAsBruHkqPQ5R71g5qdVzGq5waCm7Zl7sLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA==\"; STUDY_PERSIST=\"kR1jDZcxnohSw5v8UKhRctaBEHFrHRM0wpAW6CZRNp3Us6MLk+u/5dDs7I7+wuwLRYyCfO7dmeYkYH9evgZ+TVGaQ6FMiwp7siATddSBWseef6+fMAN5DhLjINSp2lSGmUveXmppQUzPFmneDOsmwxUKiT+YMPwCR6WxpJJRyw+8yQ70F+ClzJS/yIxAnlsIWem4V0ikHFr/EI1uZ/2fNWLXTpQdnuvatQT8FbzNggDZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU=\"; DICT_SESS=v2|7mHe6giZ2RYA0fkA0MQS0zWOLqFhfqy0JyRMkYhMg40gF0fJKhfpZ0zG0HJSOMg40PLO4kfkM6L0gu0fzM64wu0OEnfUfhM6F0; DICT_LOGIN=1||1656223239680; NETEASE_WDA_UID=1453061710#|#1611456020195; NTES_STUDY_YUNXIN_ACCID=s-1453061710; NTES_STUDY_YUNXIN_TOKEN=09261a82a7d73dbe17ce8b7aa6377359; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9rZS5zdHVkeS4xNjMuY29tL2NvdXJzZS9kZXRhaWwvNTkwMjA/UGR0PXlka1dlYg==; courseId=59079; lessonId=3044651; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1656246830; hb_MA-BFF5-63705950A31C_source=ke.study.163.com; JSESSIONID=B52EE01640D14850670522C6A4C06EB5"
    }

    resp = requests.get(url, headers=headers)
    # print(resp.text)

    f = open(f"downloadlist.txt", mode="w")

    obj = re.compile(r'window.lesson =(?P<lst>.*}])', re.S)
    tmp = obj.finditer(resp.text)
    for it in tmp:
        lst = it.group("lst")
    res = json.loads(lst)
    # res is list which only has one element i.e dict
    # print(res)
    # title0 = res[0]["title"]
    for it in res[0]["list"]:  # it is for each unit e.g '基础词汇讲义', 'Unit1'

        # print(type(it))
        title1 = it.get('title')  # '基础词汇讲义', 'Unit1'
        print(f"{title1}*****************************************************************************")
        print(it)

        for i in it['list']: # i is each section e.g '附录1' under '基础词汇讲义' ; E01·从abandon到abolish under Unit 1

            lessonId = i.get('id')
            title1_1 = i.get('title').replace('|','') # 'E01·从abandon到abolish'
            print(f"{title1}_{title1_1}****************************************************************")
            if i.get('material'):
                # download the PDF file
                url_pdf = i.get('material')
                resp_pdf = requests.get(url_pdf,headers=headers)
                fileprefix = f'{title1}_{title1_1}'
                file = f'{fileprefix}.pdf'
                print(f'{file} is downloading')
                # with open(f"{file}", mode="wb") as f:
                #     f.write(resp_pdf.content)
                print(f'{file} saved')

            if i.get('list'):
                for j in i.get('list'): # each is the breakdown under  E01·从abandon到abolish
                    title1_1_1 = j.get('title').replace('|','')
                    print(f"{title1}_{title1_1}_{title1_1_1}**********************************************************")
                    if j.get('video'):
                        id1_1_1 = j.get('id')
                        # https://ke.study.163.com/course/video.json?lessonId=104575618&r=1656251042305
                        url_video = f'https://ke.study.163.com/course/video.json?lessonId={id1_1_1}'
                        print(url_video)
                        resp_video = requests.get(url_video, headers=headers)
                        resp_video.encoding = resp_video.apparent_encoding
                        # print(resp_video.text)

                        if not resp_video.json() or resp_video.json().get('success') is False:
                            print(f'Not data returned from url {url_video}')
                            continue

                        url_mp4 = resp_video.json().get('result').get('videoUrl')
                        print(f"url_mp4 is {url_mp4}")
                        title1_1_1_ = resp_video.json().get('result').get('lessonTitle').replace('|','')
                        lessonTitle = f'{title1}_{title1_1}_{title1_1_1_}'
                        print(f'get {lessonTitle} video data starting.......')
                        resp_video.close()

                        # download
                        # resp_mp4 = requests.get(url_mp4, headers=headers)
                        # with open(f"{lessonTitle}.mp4", mode="wb") as f:
                        #     f.write(resp_mp4.content)
                        # print(f'{lessonTitle}.mp4 saved')
                        # resp_mp4.close()

                        # further handle mp4 as hit 403 error

                        f.write(f'{url_mp4}                                                             {lessonTitle}\n')
                        print(f'{url_mp4}        {lessonTitle} writen')

                    if j.get('url'):
                        # https://ke.study.163.com/cms/download/35104?seriesId=&noCache=true&api_version=2.1
                        articleId = j.get('articleId')
                        url_article = f'https://ke.study.163.com/cms/download/{articleId}?seriesId=&noCache=true&api_version=2.1'
                        print(f'url-article is {url_article}')
                        # getSubSeries(url_article)

def getwords2(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
        "cookie": "___rl__test__cookies=1656309923152; _ntes_nnid=d210a1ed73ac8d49791dd9e007b8a7e7,1634192367969; _ntes_nuid=d210a1ed73ac8d49791dd9e007b8a7e7; UM_distinctid=17fbfa77430187-0d1d26d2b671fc-5617185b-100200-17fbfa77431f41; vinfo_n_f_l_n3=3cc07e6b80b1c971.1.0.1648187892685.0.1648187967384; EDUWEBDEVICE=398a0755db534b7f8b428017d18913a2; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; sideBarPost=1970; xuetangvendor=ykt_store_xiaomi; keoutvendor=; ke_Pdt=ydkWeb; ke_inLoc=; OUTFOX_SEARCH_USER_ID_NCOO=1288925762.7441041; NTES_YD_PASSPORT=1MO6bF40jEdNWQmQ2SrNYG.BnXt1obLPnVlWa0Jp.NnlceKDcQzbiWZz7LqFIzWscvbNIuHnb9RDQK9sLCGpRVd.7o51FRZ7XFbDBOFGCrKDL9LIabrmqyO.KoVrMukkvgldIL97L8WolUSEVMb91EuNp6w9vqfnN_MyUUt.vzDy2xwScGHR18UfD5xbPtuR8W0r2kYL9xiATUg8xmzT9A5Hx; P_INFO=13828460875|1656223239|1|study|00&99|null&null&null#gud&440100#10#0#0|&0|null|13828460875; NTESSTUDYSI=ab92a0adcd0e4c08b003af4a038a0db1; STUDY_INFO=\"yd.a3d7bb5d90db452b8@163.com|8|1453061710|1656309682137\"; STUDY_SESS=\"ewwZXGPJCgIdhQZyKlAivbZNqDfdcnEYZC/3PYNvIPK7ARHbjp0KbtBiBQalOelEd576j8fTOQCEVtBIlPoDXqF5GlQExgPUf7V7um5mOPDnQnlS2AxfdgHgZzoYiNLgxX/PMLObuQ42wEi+5bapRia6P6tFClHMzzmWa6WFFTULhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA==\"; STUDY_PERSIST=\"kR1jDZcxnohSw5v8UKhRctaBEHFrHRM0wpAW6CZRNp3Us6MLk+u/5dDs7I7+wuwLRYyCfO7dmeYkYH9evgZ+TVGaQ6FMiwp7siATddSBWseyDNVsUJeKH4fkKfxxHQZ/ehXrCCy57DlSvlHpuW1E19nHRcWf3u0TGyFfthj3Qv4fEek0ZhdcJxTG1W7arGlZKHMP4hWNtrKY5k0E7e39qmJy8j26A3t0u09U6yAvTDfZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU=\"; DICT_SESS=v2|C72VrrzF2RkGn4YEhHPLRJBk4UMkfQS0ez0HJyh4pBR6BO4YGRHTu06uOMqLRHpK0zMkfUMkMYm0gK0HUfRMTF0zYO4TS0fYE0; DICT_LOGIN=1||1656309682196; NETEASE_WDA_UID=1453061710#|#1611456020195; NTES_STUDY_YUNXIN_ACCID=s-1453061710; NTES_STUDY_YUNXIN_TOKEN=09261a82a7d73dbe17ce8b7aa6377359; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9zdHVkeS4xNjMuY29tLw==; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1655953652,1656002346,1656210125,1656309709; hb_MA-BFF5-63705950A31C_source=ke.study.163.com; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1656309923; JSESSIONID=6FA4FFBA18B4642BE39D17AA60CBBDA7"
    }

    resp = requests.get(url, headers=headers)
    # print(resp.text)

    f = open(f"downloadlist2.txt", mode="w")
    #https://live.study.163.com/live/index.html?courseId=59083&lesson=3045085&type=1
    obj = re.compile(r'window.lesson =(?P<lst>.*}])', re.S)
    tmp = obj.finditer(resp.text)
    for it in tmp:
        lst = it.group("lst")
    res = json.loads(lst)
    # res is list which only has one element i.e dict   方法与实战
    print(res)
    title0 = res[0]["title"] # 方法与实战
    for it in res[0]["list"]:  # ie. 方法篇,  实战篇

        # print(type(it))
        title1 = it.get('title')  # 方法篇,  实战篇
        print(f"{title0}_{title1}*********************************************************************")
        print(it)

        for i in it['list']: # i is each section e.g '了解这条基本原则，发现背词新大陆' under '方法篇'
            title1_1 = i.get('title').replace('|','') # '了解这条基本原则，发现背词新大陆'
            print(f"{title0}_{title1}_{title1_1}*************************************************")
            if i.get('video'):
                id1_1_1 = i.get('id')
                # https://ke.study.163.com/course/video.json?lessonId=3045085&r=1656251042305
                url_video = f'https://ke.study.163.com/course/video.json?lessonId={id1_1_1}'
                print(url_video)
                resp_video = requests.get(url_video, headers=headers)
                # resp_video.encoding = resp_video.apparent_encoding
                # print(resp_video.text)

                if not resp_video.json() or resp_video.json().get('success') is False:
                    print(f'Not data returned from url {url_video}')
                    continue

                url_mp4 = resp_video.json().get('result').get('videoUrl')
                print(f"url_mp4 is {url_mp4}")
                title1_1_1_ = resp_video.json().get('result').get('lessonTitle').replace('|', '')
                lessonTitle = f'{title1}_{title1_1_1_}'
                print(f'get {lessonTitle} video data starting.......')
                resp_video.close()

                # download
                resp_mp4 = requests.get(url_mp4, headers=headers)
                # with open(f"{lessonTitle}.mp4", mode="wb") as f:
                #     f.write(resp_mp4.content)
                # print(f'{lessonTitle}.mp4 saved')
                resp_mp4.close()

                # further handle mp4 as hit 403 error

                f.write(f'{url_mp4}                                                             {lessonTitle}\n')
                print(f'{url_mp4}        {lessonTitle} writen')





# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    url = r'https://ke.study.163.com/course/detail/59009'
    courseId = re.search(r'\d{5}$', url).group()
    # 每日学习
    # getRecitationCamp()
    # 每周精讲
    # getRecitationCamp2(url)
    # 英语学习必备5500词（背诵营18季）
    # url_w =r'https://ke.study.163.com/course/detail/59079'
    # getwords(url_w)
    # 杨亮讲单词·方法与实战
    url_w2 = r'https://ke.study.163.com/course/detail/59083'
    getwords2(url_w2)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
