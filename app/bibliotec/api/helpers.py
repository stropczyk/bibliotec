def prepare_response(books):
    total_items = 0
    items = []

    for book in books:
        book.pop("_id", None)
        book.pop("title_lower", None)
        total_items += 1
        items.append(book)

    resp_dict = {
        "totalItems": total_items,
        "items": items
    }
    response = dict(resp_dict)

    return response
