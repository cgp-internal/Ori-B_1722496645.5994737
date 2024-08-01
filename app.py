from flask import Flask, render_template
from templates.index_html import IndexTemplate
from requirements_txt import Requirements

app = Flask(__name__)

@app.route('/<string:name>')
def hello_world(name=None):
    if name is None:
        name = "World"
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)