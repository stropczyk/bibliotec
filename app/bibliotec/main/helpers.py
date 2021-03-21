def prepare_inquiry(expression):
    expression = expression.split(' ')
    separator = '+'
    output = separator.join(expression)
    return output


def authors_list(authors):
    new_list = [author.upper() for author in authors]
    return new_list


def authors_list_manual(authors):
    authors_list = authors.split(',')
    new_list = [author.strip() for author in authors_list]
    output = [str(author).upper() for author in new_list]
    return output


def identifier_manual(type, identifier):
    identifiers = [{
        "type": type,
        "identifier": identifier
    }]
    return identifiers
