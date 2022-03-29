from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def save_file():
    if request.method == "POST":
        f = request.files['my_file']
        f.save('my_file.name')
        # f.save(f.filename)
        return 'Файлы загружены'
    return render_template('demo3.html')

app.run()
app.run()