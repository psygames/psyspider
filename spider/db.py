import pymongo
import pymongo.errors
from spider import db_setting
from datetime import date

db: pymongo.MongoClient = None
raw: pymongo.collection.Collection = None


def __init_db():
    client = pymongo.MongoClient(host=db_setting.host, port=db_setting.port
                                 , username=db_setting.username, password=db_setting.password)
    global db
    db = client['spider']

    collections = db.list_collection_names()
    if 'raw' not in collections:
        db['raw'].create_index([('id', 1)], unique=True)

    return db


def init():
    global db
    if db is None:
        __init_db()
    return db


def __insert(docs):
    try:
        raw.insert_one(docs)
    except pymongo.errors.DuplicateKeyError:
        return False
    return True


def raw_set(_id, title: str, year: int, state: str, tags: list, cast: list, category: str, area: str, update_date: date,
            alias: list, hot: int, story: str, urls: list):
    try:
        raw.insert_one({'id': _id, 'title': title, 'year': year, 'state': state, 'tags': tags, 'cast': cast,
                        'category': category, 'area': area, 'update_date': update_date, 'alias': alias, 'hot': hot,
                        'story': story, 'urls': urls})
    except pymongo.errors.DuplicateKeyError:
        return False
    return True


def raw_exist(_id):
    return raw.find_one({'id': _id}) is not None
