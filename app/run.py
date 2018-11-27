from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)
env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html'])
)


@app.route('/')
def hello_world():
    return render_template('home.html',
                           message='This is the draft version of AD Manager application')


if __name__ == '__main__':
    app.run(debug=True)
