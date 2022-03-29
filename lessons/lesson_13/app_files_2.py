from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def show_form():
    return render_template('demo4.html')

@app.route('/', methods=["POST"])
def save_file():
    f = request.files['my_file']
    f.save('asd/my_new_file_name.exe')
    return 'Файлы загружены'

app.run()