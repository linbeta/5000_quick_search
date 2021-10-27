'''
這個檔案留個紀錄而已，第一版用來爬中籤號碼的code，
後來覺得用selenium爬運算太慢，也擔心放上GCP要跑會有問題，所以後來寫了search_v2
'''
from bs4 import BeautifulSoup as bs
from selenium import webdriver

PATH = "chromedriver.exe"

url = "https://vhpi.5000.gov.tw/"

# 先用selenium取得的網頁原始碼，丟進bs裡做成湯
driver = webdriver.Chrome(PATH)
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

newest = {}
for n, item in enumerate(css_id_list):
    newest[item[1::]] = get_draw_nums(css_id_list[n])
# print(newest)

# TODO: 用selenium怕無法上雲端，資料其實都存在<footer>底下的script tag裡了，改抓那裡的資料處理string來分析
# TODO: 將week_1資料存進資料庫，這樣如有新增資料只需要刷過一次就可以了



