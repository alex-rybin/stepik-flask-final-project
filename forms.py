from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, IntegerField
from wtforms.validators import InputRequired

from constants import DifficultyOptions


class StartGame(FlaskForm):
    difficulty = RadioField(
        'Сложность', choices=DifficultyOptions.get_choices(), default=DifficultyOptions.EASY
    )
    start_button = SubmitField('Начать')


class AnswerForm(FlaskForm):
    answer = IntegerField('Ответ', validators=(InputRequired(),))
    submit = SubmitField('Отправить')
