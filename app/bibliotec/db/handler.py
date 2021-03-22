import os

from bson.objectid import ObjectId

from pymongo import MongoClient

db_user = os.getenv('DB_USER')
db_pwd = os.getenv('DB_PWD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

client = MongoClient(f'mongodb+srv://{db_user}:{db_pwd}@{db_host}/{db_name}?retryWrites=true&w=majority')
db = client[db_name]
col = db['books']


def insert_in_col(title, authors, published_date, identifiers, page_count, image_link, language):
    col.insert_one({
        'title': title,
        'title_lower': title.lower(),
        'authors': authors,
        'publishedDate': published_date,
        'identifiers': identifiers,
        'pageCount': page_count,
        'image': image_link,
        'language': language
    })


def import_to_col(title, authors, published_date, identifiers, page_count, image_link, language):
    col.insert_one({
        'title': title,
        'title_lower': title.lower(),
        'authors': authors,
        'publishedDate': published_date,
        'identifiers': identifiers,
        'pageCount': page_count,
        'image': image_link,
        'language': language
    })


def check_if_exist(isbn):
    book = col.find_one({"identifiers": {'$elemMatch': {'identifier': {'$regex': isbn.data}}}})
    return book


def find_book(identifier):
    book = col.find_one({"identifiers": {'$elemMatch': {'identifier': identifier}}})
    return book


def update_book(book_id, title, authors, published_date, page_count, image_link, language):
    update = col.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": {
            'title': title,
            'title_lower': title.lower(),
            'authors': authors,
            'publishedDate': published_date,
            'pageCount': page_count,
            'image': image_link,
            'language': language
        }}
    )
    return update


def find_books(params):
    books = col.find(params)
    return books
