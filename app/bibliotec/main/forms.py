from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, URL, ValidationError, Optional

from bibliotec.db.handler import *


class AddForm(FlaskForm):
    title = StringField(label='Tytuł',
                        validators=[DataRequired()])
    authors = StringField(label='Autor/Autorzy',
                          validators=[DataRequired()],
                          description='W przypadku kilku autorów jako separatora użyj znaku ","')
    published_date = StringField(label='Data publikacji',
                                 validators=[DataRequired()],
                                 description='Wprowadź datę w formacie YYYY')
    isbn = StringField(label='Kod ISBN',
                       validators=[DataRequired()])
    isbn_type = StringField(label='Typ kodu ISBN',
                            validators=[DataRequired()],
                            description='np. ISBN-13')
    page_count = IntegerField(label='Liczba stron',
                              validators=[DataRequired(), NumberRange(min=1)])
    image = StringField(label='Link od okładki',
                        validators=[URL(), Optional()])
    language = StringField(label='Język publikacji',
                           validators=[DataRequired()])
    submit = SubmitField(label='Dodaj książkę')

    def validate_isbn(self, isbn):
        book = check_if_exist(isbn)
        if book:
            raise ValidationError('Książka o tym numerze ISBN już funkcjonuje w katalogu.')


class EditForm(FlaskForm):
    title = StringField(label='Tytuł',
                        validators=[DataRequired()])
    authors = StringField(label='Autor/Autorzy',
                          validators=[DataRequired()],
                          description='W przypadku kilku autorów jako separatora użyj znaku ","')
    published_date = StringField(label='Data publikacji',
                                 validators=[DataRequired()],
                                 description='Wprowadź datę w formacie YYYY')
    page_count = IntegerField(label='Liczba stron',
                              validators=[DataRequired(), NumberRange(min=1)])
    image = StringField(label='Link od okładki',
                        validators=[URL(), Optional()])
    language = StringField(label='Język publikacji',
                           validators=[DataRequired()])
    submit = SubmitField(label='Zapisz zmiany')
