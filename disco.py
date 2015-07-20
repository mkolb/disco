import logging
import sqlite3
from flask import Flask, url_for, render_template, make_response, redirect, request, session, escape
from contextlib import closing
app = Flask(__name__)
app.debug = True

app.config.from_object(__name__)

responses = []
responses.append(('Cheese', 'INTERCEPTOR'))
responses.append(('Men', 'TINA'))
responses.append(('Cereal', 'HUMAN'))
responses.append(('Souls', 'FIGHTER'))

questions = [['When I wake up in the morning I like to consume...', responses]]

responses = []
responses.append(('Kramer', 'HUMAN'))
responses.append(('George', 'INTERCEPTOR'))
responses.append(('Crazy Joe Devola', 'FIGHTER'))
responses.append(('Puddy', 'TINA'))

questions.append(['My favorite Seinfeld character is...', responses])

responses = []
responses.append(('Sunflower', 'HUMAN'))
responses.append(('Hummingbird', 'INTERCEPTOR'))
responses.append(('Boll Weevil', 'FIGHTER'))
responses.append(('Unicorn', 'TINA'))

questions.append(['My favorite living creature is...', responses])
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/q/<int:question_id>', methods=['GET','POST'])
def display_question(question_id):
    if request.method == 'POST':
        session['question_' + str(question_id -1)] = request.form['r']
    if question_id > len(questions) - 1:
        return redirect(url_for('spirit_animal'))
    resp = make_response(render_template('question.html', q=questions[question_id], r=questions[question_id][1], id=question_id))
    return resp

@app.route('/spirit_animal')
def spirit_animal():
    def calculate_animal():
        return escape(session['question_0'])
    return render_template('spirit_animal.html', animal=calculate_animal())


if __name__ == '__main__':
    app.run()

app.secret_key = 'SKLDJF804208sdklzklsjdf'
