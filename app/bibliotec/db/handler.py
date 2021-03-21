from pymongo import MongoClient

client = MongoClient('mongodb+srv://guest:guest-password@database.pjbt9.mongodb.net/bibliotec?retryWrites=true&w=majority')
db = client['bibliotec']
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
