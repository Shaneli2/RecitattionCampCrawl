# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import requests
import re

def main():
    headers ={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"
    }
    url ='https://ke.study.163.com/course/detail/59009?Pdt=ydkWeb'
    resp = requests.get(url,headers=headers)
    resp.encoding = resp.apparent_encoding
    print(resp.text)
    obj = re.compile(r'^<!*',re.S)
    mp3_url = obj.search(resp.text)
    url2= obj.findall(resp.text)
    print(url2)

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #print_hi('PyCharm')
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
