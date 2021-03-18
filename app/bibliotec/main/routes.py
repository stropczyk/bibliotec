from flask import Blueprint, render_template

from bibliotec.db.handler import col

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home", methods=['GET'])
def home():
    # db_book_body = {
    #     'title': title,
    #     'authors': authors,
    #     'publishedDate': published_date,
    #     'ISBN_13': ISBN_13,
    #     'ISBN_10': ISBN_10,
    #     'pageCount': pages,
    #     'image': image_link,
    #     'language': language
    # }

    # db_book_body = {
    #     'title': 'title',
    #     'authors': 'authors',
    #     'publishedDate': 'published_date',
    #     'ISBN_13': 'ISBN_13',
    #     'ISBN_10': 'ISBN_10',
    #     'pageCount': 'pages',
    #     'image': 'image_link',
    #     'language': 'language'
    # }
    #
    # col.insert_one(db_book_body)

    return render_template('home.html', title='home')


@main.route("/catalogue")
def catalogue():
    return render_template('catalogue.html', title='Katalog książek')


@main.route("/newitem")
def new_item():
    return render_template('add.html', title='Dodaj książkę')


@main.route("/import")
def import_book():
    return render_template('import.html', title='Importuj książkę')
