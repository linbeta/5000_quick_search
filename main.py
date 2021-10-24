from flask import Flask, render_template, request
import search_v2

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def show_result():
    if request.method == 'GET':
        return f"The URL /result is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form
        user_input = form_data['last_3_digits']
        # 連結到search_v2.py這份檔案進行搜尋的運算，用for loop跑四周的比對
        results = []
        for week in search_v2.weeks:
            # 回傳results作為搜尋檢查，排除單一券種重複中籤的狀況
            result = search_v2.scan(user_input, week, results)
            results.append(result)
        # 將結果轉成中文輸出
        results_zh_tw = [
            f"第{i + 1}周-抽中{search_v2.zh_tw[name]}" if name in search_v2.zh_tw else f"第{i + 1}周-{name}" for i, name in enumerate(results)]
        return render_template('result.html', form_data=form_data, search_result=results_zh_tw)


if __name__ == "__main__":
    app.run(debug=True)
