from flask import Flask, render_template, request
import search

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
        # 連結到search.py這份檔案進行搜尋的運算
        result = search.scan(user_input)
        return render_template('data.html', form_data=form_data, search_result=result)


if __name__ == "__main__":
    app.run(debug=True)
