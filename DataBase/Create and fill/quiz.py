from random import randint
from flask import Flask, request, session, redirect, url_for
from db_scripts import get_question_after, get_quizes, check_answer

def save_answers():
    answer = request.form.get('ans_text')
    quest_id = request.form.get('q_id')
    session['last_question'] = quest_id
    session['total'] += 1
    if check_answer(quest_id, answer):
        session['answers'] += 1

def quizes_list():
    html = '''<html><head><title>Выбор викторины</title></head>
    <body><h2>Выберите викторину:</h2><form method="POST" action="/">
    <select name="quiz">'''
    for quiz in get_quizes():
        html += f'''<option value="{quiz[0]}">{quiz[1]}</option>'''
    html += '''</select><p><input type="submit" value="Выбрать"></p>
    </form></body></html>'''
    return html

def index():
    if request.method == 'GET':
        session['last_question'] = 0
        quiz_form = quizes_list()
        return quiz_form
    else:
        quiz_id = request.form.get('quiz')
        session['quiz'] = int(quiz_id)
        return redirect(url_for('test'))

def test():
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))

    result = get_question_after(session['last_question'], session['quiz'])
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    
    else:
        session['last_question'] = result[0]
        return '<p>' + str(result) + '</p>'

def result():
    return '<h3>Thats all :)</h3>'

app = Flask(__name__)
app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)
app.config['SECRET_KEY'] = 'sadsadsadsasadsa'

if __name__ == '__main__':
    app.run()