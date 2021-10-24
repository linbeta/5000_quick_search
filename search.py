'''
這個檔案留個紀錄而已，第一版用來爬中籤號碼的code，
後來覺得用selenium爬運算太慢，也擔心放上GCP要跑會有問題，所以後來寫了search_v2
'''
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import main

DRIVER_PATH = "D:\OneDrive\Development\Tools\chromedriver.exe"

url = "https://vhpi.5000.gov.tw/"

# 先用selenium取得的網頁原始碼，丟進bs裡做成湯
driver = webdriver.Chrome(DRIVER_PATH)
driver.get(url)

source = bs(driver.page_source, "html.parser")
driver.close()


# 定義取得中獎號碼list的function
def get_draw_nums(css_id):
    target_lis = source.select_one(css_id).find_all("li")
    win_nums = []
    for i in target_lis:
        win_nums.append(i.text)
    return win_nums


# 從網頁原始碼中抓出8種券的css id
css_id_list = ["#domesticTravel", "#iYuan", "#agriculture", "#artFunE",
               "#artFunP", "#sports", "#hakka", "#rgionalRevitalization"]

week_1 = {}
for n, item in enumerate(css_id_list):
    week_1[item[1::]] = get_draw_nums(css_id_list[n])
# print(week_1)

ch_names = ["國旅券", "i原券", "農遊券", "藝fun券-數位", "藝fun券-紙本", "動滋券", "客庄券", "地方創生券"]
zh_tw = {key: ch_names[i] for i, key in enumerate(week_1)}
# print(zh_tw)

# TODO: 用selenium怕無法上雲端，資料其實都存在<footer>底下的script tag裡了，改抓那裡的資料處理string來分析
# TODO: 將week_1資料存進資料庫，這樣如有新增資料只需要刷過一次就可以了

# Part 2: user輸入ID末3碼進行比對
# user_id = input("請輸入末三碼： ")


def scan(user_input):
    # 從week_1中獎號字典中去loop，拿每一個獎號看是否在user_id中，有的話break(這邊也可同時處理順序和無法重複中獎的問題)，印出券種
    win = False
    for key in week_1:
        for num in week_1[key]:
            if num in user_input:
                # print(f"抽中 {zh_tw[key]}")
                win = True
                return f"抽中 {zh_tw[key]}"
        # 排除重複中獎，如已經有抽中了，當周直接跳出
        if win:
            break
    if not win:
        # print("本周未中籤")
        return "本周未中籤"

# print(scan("123"))
