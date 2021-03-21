import json
import os

from urllib.request import urlopen
from flask import Blueprint, render_template, redirect, url_for, request, flash

from bibliotec.db.handler import *
from .forms import AddForm
from .helpers import *

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home", methods=['GET'])
def home():
    return render_template('home.html', title='home')


@main.route("/catalogue", methods=['GET', 'POST'])
def catalogue():
    all_books = col.find()

    if request.method == 'POST':
        inquiry_dict = {}

        if request.form['title']:
            title = request.form['title'].lower()
            inquiry_dict['title_lower'] = {'$regex': title}

        if request.form['author']:
            author = request.form['author'].upper()
            inquiry_dict['authors'] = {'$regex': author}

        if request.form['language']:
            language = request.form['language'].lower()
            inquiry_dict['language'] = language

        if request.form['date_min'] and request.form['date_max']:
            date_min = request.form['date_min']
            date_max = request.form['date_max']
            inquiry_dict['publishedDate'] = {'$gte': date_min, '$lte': date_max}
        elif request.form['date_min'] and not request.form['date_max']:
            date_min = request.form['date_min']
            inquiry_dict['publishedDate'] = {'$gte': date_min}
        elif request.form['date_max'] and not request.form['date_min']:
            date_max = request.form['date_max']
            inquiry_dict['publishedDate'] = {'$lte': date_max}

        all_books = col.find(inquiry_dict)

        return render_template('catalogue.html', title='Katalog książek', books=all_books)

    return render_template('catalogue.html', title='Katalog książek', books=all_books)


@main.route("/newitem", methods=['GET', 'POST'])
def new_item():
    form = AddForm()

    if form.validate_on_submit():
        title = form.title.data
        authors = authors_list_manual(form.authors.data)
        published_date = form.published_date.data
        identifiers = identifier_manual(form.isbn_type.data, form.isbn.data)
        page_count = form.page_count.data

        if form.image.data:
            image_link = form.image.data
        else:
            image_link = url_for('static', filename='no_foto.jpg')

        language = form.language.data

        insert_in_col(title, authors, published_date, identifiers, page_count, image_link, language)

        flash('Książka została dodana do katalogu', 'success')

        return redirect(url_for('main.home'))

    return render_template('add.html', title='Dodaj książkę', form=form)


@main.route("/import", methods=['GET', 'POST'])
def import_book():
    if request.method == 'POST':
        api_uri = f'https://www.googleapis.com/books/v1/volumes?q='

        if request.form['title']:
            title = request.form['title']
            title = prepare_inquiry(title)
            api_uri += f'+intitle:{title}'

        if request.form['author']:
            author = request.form['author']
            author = prepare_inquiry(author)
            api_uri += f'+inauthor:{author}'

        if request.form['publisher']:
            publisher = request.form['publisher']
            publisher = prepare_inquiry(publisher)
            api_uri += f'+inpublisher:{publisher}'

        if request.form['subject']:
            subject = request.form['subject']
            subject = prepare_inquiry(subject)
            api_uri += f'+subject:{subject}'

        if request.form['isbn']:
            isbn = request.form['isbn']
            api_uri += f'+isbn:{isbn}'

        if request.form['lccn']:
            lccn = request.form['lccn']
            api_uri += f'+lccn:{lccn}'

        if request.form['oclc']:
            oclc = request.form['oclc']
            api_uri += f'+oclc:{oclc}'

        response = urlopen(api_uri)
        data = json.load(response)

        if data['totalItems'] == 0:
            flash('Niestety nie znaleziono książęk o zadanych parametrach', 'danger')

            return render_template('import.html', title='Importuj książkę')

        for book in data['items']:
            book_info = book['volumeInfo']

            title = book_info.get('title', 'b.d.')

            authors = book_info.get('authors', ['b.d.'])
            if authors != ['b.d.']:
                authors = authors_list(authors)

            published_date = book_info.get('publishedDate', 'b.d.')
            identifiers = book_info.get('industryIdentifiers', [{'type': 'ISBN', 'identifier': 'b.d.'}])
            page_count = book_info.get('pageCount', 'b.d.')
            language = book_info.get('language', 'b.d.')

            image_link = book_info.get('imageLinks', 'b.d.')
            if image_link != 'b.d.':
                image_link = image_link['smallThumbnail']
            else:
                image_link = url_for('static', filename='no_foto.jpg')

            import_to_col(title, authors, published_date, identifiers, page_count, image_link, language)

        flash('Pozytywnie zaimportowano książki', 'success')

        return render_template('import.html', title='Importuj książkę')

    return render_template('import.html', title='Importuj książkę')
