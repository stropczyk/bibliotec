import json

from flask import request
from flask_restful import Resource

from bibliotec.db.handler import *
from .helpers import *

BASE_URL = "http://bibliotec.pl/books/v1/volumes"


class BooksInquiry(Resource):
    def get(self):
        title = request.args.get('intitle')
        author = request.args.get('inauthor')
        language = request.args.get('language')
        date_min = request.args.get('date_min')
        date_max = request.args.get('date_max')

        inquiry_dict = {}

        if title:
            title = title.lower()
            inquiry_dict['title_lower'] = {'$regex': title}

        if author:
            author = author.upper()
            inquiry_dict['authors'] = {'$regex': author}

        if language:
            language = language.lower()
            inquiry_dict['language'] = language

        if date_min and date_max:
            date_min = date_min
            date_max = date_max
            inquiry_dict['publishedDate'] = {'$gte': date_min, '$lte': date_max}
        elif date_min and not date_max:
            date_min = date_min
            inquiry_dict['publishedDate'] = {'$gte': date_min}
        elif date_max and not date_min:
            date_max = date_max
            inquiry_dict['publishedDate'] = {'$lte': date_max}

        books = find_books(inquiry_dict)
        response = prepare_response(books)

        return response
