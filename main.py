from flask import Flask, render_template, request
import search_v2

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        user_input = form_data['last_3_digits']
        # 連結到search_v2.py這份檔案進行搜尋的運算，用for loop跑四周的比對
        results = []
        for week in search_v2.weeks:
            result = search_v2.scan(user_input, week)
            results.append(result)
        return render_template('data.html', form_data=form_data, search_result=results)


if __name__ == "__main__":
    app.run(debug=True)
