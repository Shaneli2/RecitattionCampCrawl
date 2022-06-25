# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import requests
import re
import json

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44",
}

# 杨亮讲英文·全民英语背诵营  https://ke.study.163.com/course/detail/59009
def ｇetRecitationCamp(url=r'https://ke.study.163.com/course/detail/59009'):
    resp = requests.get(url, headers=headers)
    #print(resp.text)

    obj = re.compile(r'window.lesson =(?P<list>.*}])', re.S)
    tmp = obj.finditer(resp.text)
    for it in tmp:
        list = it.group("list")
        print(list)
        print(type(list))
    res = json.loads(list)

    # res[0] :　新人必读
    # res[１] :　每日学习
    # res[２] :　每周精讲
    # for it in res:
    #     print("*****")
    #     print(f"the type is {type(it)}")
    #     print(it)
    print(res[1])

# refer "https://ke.study.163.com/topic/study/article/index.html?pid=16096&courseId=59009&lessonId=3040763#/"
def getSubSeries(url):   #url ='https://ke.study.163.com/cms/api/16096'
    resp = requests.get(url,headers=headers)
    resp.encoding = resp.apparent_encoding
    print(resp.json())
    title = resp.json()["title"].replace('|', '')

    obj = re.compile(r'[a-zA-z]+://[^\s]*mp4',re.S)
    obj2 = re.compile(r'[a-zA-z]+://[^\s]*mp3', re.S)

    url_mp4 = obj.findall(resp.text)
    url_mp3 = obj2.findall(resp.text)
    print(url_mp4)
    print(url_mp3)
    resp.close()

    #download
    i = 0
    for a in url_mp4:
        i = i + 1
        resp_mp4 = requests.get(a,headers=headers)
        with open(f"{title}_{i}.mp4", mode="wb") as f:
            f.write(resp_mp4.content)
        resp_mp4.close()

    i = 0
    for a in url_mp3:
        i = i+1
        resp_mp3 = requests.get(a,headers=headers)
        with open(f"{title}_{i}.mp3", mode="wb") as f:
            f.write(resp_mp3.content)
        resp_mp3.close()



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #print_hi('PyCharm')
    #GetSubSeries(r'https://ke.study.163.com/cms/api/16096')
    ｇetRecitationCamp()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
