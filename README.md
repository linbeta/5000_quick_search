# 五倍券數位綁定加碼券中籤查詢小工具

上週看到有人做了一個一個[查詢工具](https://onlinemad.github.io/5000-lottery/)，看了以後手癢想說用Python來寫寫看應該很好玩，就動手做了。

官方的查詢系統需要輸入完整身分證字號和健保卡號，還要圖形驗證碼，查起來很麻煩。這個簡易查詢只需要輸入身分證末三碼就可以查了。

## App link and screenshots

這兩天順便練習用GCP來deploy這個小app，網址：https://quick-search-5-yfntlql7tq-de.a.run.app

<img src="/ScreenShots/home.PNG" width="350"> <img src="/ScreenShots/result.PNG" width="350">

## 版本更新紀錄

- 10/26 增加除錯功能： 如果即時爬取官網資料出問題時，會使用備援json檔來讀取中獎號碼備份，至少網站不會掛掉。
- 10/27 更新script parsing規則(多4個空格)&手動增加備援json檔中籤號碼。目前看來官網新增中獎號碼時，script裡面的空白欄位會變動(怕)，一直改code不是辦法XD，需要設計新的備援方案...
- 10/28 引用第一版的search.py來取得備援資料

### 參考資料
[Python Web Scraping: JSON in SCRIPT tags](https://www.youtube.com/watch?v=QNLBBGWEQ3Q)

[How to get JavaScript variables from a script tag using Python and Beautifulsoup](https://stackoverflow.com/questions/51777725/how-to-get-javascript-variables-from-a-script-tag-using-python-and-beautifulsoup/51778105)

[Convert a String representation of a Dictionary to a dictionary?](https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary)

[振興五倍券加碼券速查](https://github.com/onlinemad/5000-lottery)

[Build and deploy a Flask application on Google Cloud Run - Part 2 - Deploy a Python service](https://www.youtube.com/watch?v=v-9R1LaSQiw)
