import requests
from bs4 import BeautifulSoup
import ast
import search

url = "https://vhpi.5000.gov.tw/"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
script = soup.find_all("script")[-1].text.split("\n\n        var ")
# print(script)

try:
    # 第一周中獎號：winNo1
    winNo1_str = script[0].split("\n        var ")[1].split(" = ")[1]
    # converted a formatted string into a dictionary
    winNo1 = ast.literal_eval(winNo1_str)
    # print(winNo1)

    # 第二周中獎號碼：winNo2
    winNo2_str = script[1].split("\n\n\tvar ")[0].split(" = ")[1]
    winNo2 = ast.literal_eval(winNo2_str)
    # print(winNo2)

    # 第三周中獎號碼：winNo3
    # TODO: if crash, check here to update parsing
    winNo3_str = script[2].split("\n\n\tvar ")[0].split(" = ")[1].split(";")[0]
    winNo3 = ast.literal_eval(winNo3_str)
    # print(winNo3)

    # 第四周中獎號碼：winNo4 (注意這種string的切法後面要切乾淨，丟進ast.literal_eval時才能做出正確的dictionary
    winNo4_str = script[3].split("\n\n        window.")[0].split(" = ")[1]
    winNo4 = ast.literal_eval(winNo4_str)
    # print(winNo4)
except:
    print("failed")
    # 如果出錯，使用search.py的程式用selenium來取得獎號
    winNo4 = search.newest

    # 如果官網原始資料有異動而出錯，直接挖備援檔案winNo.json裡的資料來用
    # with open("winNo.json", "r") as backup_data:
    #     data = json.load(backup_data)
    #     winNo1 = data["winNo1"]
    #     winNo2 = data["winNo2"]
    #     winNo3 = data["winNo3"]
    #     winNo4 = data["winNo4"]
    # TODO: 出錯時寄個email通知我


# 把每周中獎號字典存成list方便後續使用
weeks = [winNo1, winNo2, winNo3, winNo4]
# print(weeks)

# 轉換為票券中文名稱
ch_names = ["國旅券", "i原券", "農遊券", "藝fun券-數位", "藝fun券-紙本", "動滋券", "客庄券", "地方創生券"]
zh_tw = {key: ch_names[i] for i, key in enumerate(winNo1)}
# print(zh_tw)


# Define search function
def scan(user_input, winNo, ticket_list):
    '''
    從winNo1~winNo4中獎號字典中去loop，拿每一個獎號看是否在user_id中，有的話break(這邊也可同時處理順序和無法重複中獎的問題)，印出券種。
    ticket_list用來追蹤已中籤的券種，排除同一券種重複中獎問題，在main中存在results中。
    '''
    win = False
    for key in winNo:
        for num in winNo[key]:
            if num in user_input and num[-2] == user_input[-2] and key not in ticket_list:
                win = True
                return key
        # 排除當周重複中獎，如已經有抽中了，當周直接跳出
        if win:
            break
    if not win and len(winNo) == 0:
        return "尚未公布"
    elif not win and len(winNo) < 8:
        return "未中籤-還有機會"
    else:
        return "未中籤"
