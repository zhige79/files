import requests
import fake_useragent
from bs4 import BeautifulSoup
import random
import os
import time
from tools import list_processing
import xlsxwriter


# 数据处理
def data_processing(data):      # 此处参数应传入一个列表和一个数字
    split_list = list_processing.list_of_groups(data, 14)       # 利用该方法以每14个一组的规律拆分数据
    work_book = xlsxwriter.Workbook("market.xlsx")
    work_sheet = work_book.add_worksheet("Sheet1")
    for columns in range(len(split_list)):      # 竖列循环
        for row in range(14):                   # 横行循环
            work_sheet.write(columns, row, split_list[columns][row])
    work_book.close()


if __name__ == '__main__':
    ua = fake_useragent.UserAgent()
    print("开始！")
    print("正在获取代理：。。。")
    os.system('python tools/ip.py')
    print('获取成功！')
    page = int(input('你需要爬取前多少页？(推荐50页以下)\n'))
    c = []
    with open('ip.txt', 'r') as fi:
        l = fi.read().split(" ")
        c.append(l)
    c = c[0]
    headers = {
        'User-Agent': str(ua.random),
        'Host': 'q.10jqka.com.cn',
        'Referer': 'http://q.10jqka.com.cn/',
        'X-Requested-With': 'XMLHttpRequest',
    }
    # 代理池，请勿删本程序包内未知文件
    proxies = {
        'https': random.choice(c)
    }
    try:
        main_list1 = []
        for a in range(page):
            url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/' + str(a + 1) + '/ajax/1/'
            response = requests.get(url, headers=headers, proxies=proxies)
            if response.status_code != 200:
                print("获取第" + str(page) + "失败，已重试")
                page = page-1
                continue
            response = response.text
            time.sleep(1)
            print("正在爬取第" + str(a + 1) + "页")
            soup = BeautifulSoup(response, 'lxml')
            clean = soup.find('table').text     # 找到源代码里的table标签里的文字内容
            clean = clean.split('\n')           # 使用split方法分割字符串
            clean.remove('加自选')              # 剔除无用列
            cleaner = [x for x in clean if x != '']     # 列表推导式判断
            main_list1.append(cleaner)
            # print(np.array(cleaner))
        for i in main_list1[1:]:
            del i[:14]
        main_list2 = list_processing.list_bond(main_list1)      # 此处已将所有需要的数据读取到main_list2中了
        # 接下来将数据全部记录到excel中
        data_processing(main_list2)
    except TimeoutError:
        print('请求超时，请重新运行本程序！')
    except WindowsError:
        print('未知错误，请重新运行！')
    except BaseException:
        print('未知错误，请重新运行！')
    finally:
        print("结束，请查看market.xlsx文件获取数据！谢谢使用！")
        os.system('del ip.txt')                 # 文件回收
