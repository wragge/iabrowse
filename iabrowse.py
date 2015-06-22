import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient, ASCENDING, DESCENDING
from bson.son import SON
from flask.ext.paginate import Pagination

MONGOLAB_URL = os.environ['MONGOLAB_URL']

app = Flask(__name__)


def get_db():
    dbclient = MongoClient(MONGOLAB_URL)
    db = dbclient.get_default_database()
    return db


@app.route('/')
def list_series():
    pipeline = [
        {"$group": {"_id": "$series", "items": {"$sum": 1}}},
        {"$project": {"_id": 0, "series": "$_id", "items": "$items"}},
        {"$sort": SON([("series", 1)])}
    ]
    db = get_db()
    series = db.items.aggregate(pipeline)
    print series
    return render_template('list_series.html', series=series['result'])


@app.route('/browse')
def browse_series():
    series = request.args.get('series', None)
    print series
    if not series:
        return redirect(url_for('list_series'))
    else:
        control = request.args.get('control', None)
        db = get_db()
        if control:
            items = db.items.find({'series': series, 'control_symbol': control, 'digitised_status': True}).limit(1)
        else:
            items = db.items.find({'series': series, 'digitised_status': True}).sort('control_symbol', ASCENDING).limit(1)
        item = items[0]
        identifier = item['identifier']
        control = item['control_symbol']
        print control
        images = db.images.find({'identifier': identifier}).sort('page', 1)
        next = db.items.find({'series': series, 'control_symbol': {'$gt': control}, 'digitised_status': True}).sort('control_symbol', ASCENDING).limit(1)
        try:
            next_item = next.next()
        except StopIteration:
            next_item = None
        previous = db.items.find({'series': series, 'control_symbol': {'$lt': control}, 'digitised_status': True}).sort('control_symbol', DESCENDING).limit(1)
        try:
            previous_item = previous.next()
        except StopIteration:
            previous_item = None
        return render_template('list_items.html', item=item, next_item=next_item, previous_item=previous_item, images=images)


if __name__ == '__main__':
    app.run(debug=True)