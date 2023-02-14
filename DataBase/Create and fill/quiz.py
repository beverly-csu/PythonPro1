from random import randint
from flask import Flask, render_template, request, session, redirect, url_for
from db_scripts import get_question_after, get_quizes, check_answer

def save_answers():
    answer = request.form.get('ans_text')
    quest_id = request.form.get('q_id')
    session['last_question'] = quest_id
    session['total'] += 1
    if check_answer(quest_id, answer):
        session['answers'] += 1

def index():
    if request.method == 'GET':
        session['last_question'] = 0
        return render_template('start.html', q_list=get_quizes())
    else:
        quiz_id = request.form.get('quiz')
        session['quiz'] = int(quiz_id)
        return redirect(url_for('test'))

def test():
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))

    result = get_question_after(session['last_question'], session['quiz'])
    if request.method == 'POST':
        save_answers()

    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    
    else:
        session['last_question'] = result[0]
        answers_list = [result[2], result[3], result[4], result[5]]
        from random import shuffle
        shuffle(answers_list)
        return render_template('test.html', quest_id=result[0], question=result[1], answers_list=answers_list)

def result():
    return '<h3>Thats all :)</h3>'

import os
app = Flask(__name__, template_folder=os.getcwd(), static_folder=os.getcwd())
app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test, methods=['GET', 'POST'])
app.add_url_rule('/result', 'result', result)
app.config['SECRET_KEY'] = 'sadsadsadsasadsa'

if __name__ == '__main__':
    app.run()