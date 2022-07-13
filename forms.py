from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, IntegerField, StringField
from wtforms.validators import InputRequired, Length

from constants import DifficultyOption


class StartGame(FlaskForm):
    difficulty = RadioField(
        'Сложность', choices=DifficultyOption.get_choices(), default=DifficultyOption.EASY
    )
    name = StringField('Ваше имя', validators=(InputRequired(), Length(min=3)))
    start_button = SubmitField('Начать')


class AnswerForm(FlaskForm):
    answer = IntegerField('Ответ', validators=(InputRequired(),), default=0)
    submit_answer = SubmitField('Отправить')
