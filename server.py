from flask import Flask, render_template, request, redirect, session, flash, url_for
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECEST_KEY', 'for dev')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    print(type(request.form), " this is form")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['pronouns'] = request.form['pronouns']
    if 'subscribe' in request.form:
        session['subscribe'] = "You Subscribed!"
    else:
        session['subscribe'] = "Please Subscribe Us!"
    print(session['subscribe'])
    return redirect('/result')


@app.route('/result')
def result():
    name = session['name']
    location = session['location']
    language = session['language']
    comments = session['comments']
    pronouns = session['pronouns']
    subscribe = session['subscribe']

    return render_template('result.html', name=name, location=location, language=language, comments=comments, pronouns=pronouns, subscribe=subscribe)


@app.route('/go_home')
def go_home():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
