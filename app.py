from flask import Flask, render_template, request, redirect, url_for, session

from config import Config
from constants import GAME_DESCRIPTION, LIVES, LOST_GAME_MESSAGE, DifficultyOption
from forms import StartGame, AnswerForm
from logic import generate_expression

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    kwargs = {
        'form': StartGame(),
        'description': GAME_DESCRIPTION,
    }
    error = request.args.get('error')
    if error:
        kwargs['error'] = error

    return render_template('index.html', **kwargs)


@app.route('/start-game/', methods=('post',))
def start_game():
    difficulty = request.form.get('difficulty')
    name = request.form.get('name')

    if not difficulty:
        return redirect(url_for('index', error='Не указана сложность'))
    if not name:
        return redirect(url_for('index', error='Не указано имя'))
    else:
        session['lives'] = LIVES
        session['name'] = name
        return redirect(url_for('game', difficulty=difficulty))


@app.route('/game/<string:difficulty>/', methods=('post', 'get'))
def game(difficulty: str):
    expression, expected_answer = generate_expression(DifficultyOption(difficulty))
    render_kwargs = {
        'form': AnswerForm(),
        'expression': expression,
        'difficulty': difficulty,
    }

    answer = request.form.get('answer')

    if answer is not None:
        if answer.isnumeric():
            answer = int(answer)
        if session['expected_answer'] == answer:
            render_kwargs.update(
                {
                    'result_class': 'bg-success',
                    'previous_result': 'Верно',
                }
            )
        else:
            session['lives'] -= 1
            if session['lives'] == 0:
                return render_template(
                    'game_end.html',
                    fail_message=LOST_GAME_MESSAGE.format(name=session['name']),
                )
            else:
                session['answer'] = expected_answer
                render_kwargs.update(
                    {
                        'result_class': 'bg-danger',
                        'previous_result': 'Неправильно',
                    }
                )

    session['expected_answer'] = expected_answer
    render_kwargs['lives'] = session['lives']
    return render_template('game_page.html', **render_kwargs)


if __name__ == '__main__':
    app.run()
