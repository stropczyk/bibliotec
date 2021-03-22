import requests

from flask import Blueprint, render_template, redirect, request

from .handler import BASE_URL

apis = Blueprint('apis', __name__)


@apis.route('/apis', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        inquiry_dict = {}

        if request.form['title']:
            title = request.form['title'].lower()
            inquiry_dict['intitle'] = title

        if request.form['author']:
            author = request.form['author'].lower()
            inquiry_dict['inauthor'] = author

        if request.form['language']:
            language = request.form['language'].lower()
            inquiry_dict['language'] = language

        if request.form['date_min']:
            date_min = request.form['date_min']
            inquiry_dict['date_min'] = date_min

        if request.form['date_max']:
            date_max = request.form['date_max']
            inquiry_dict['date_max'] = date_max

        url_resp = requests.get(BASE_URL, params=inquiry_dict)
        url = url_resp.url

        return redirect(url, code=302)

    return render_template('apis.html')
