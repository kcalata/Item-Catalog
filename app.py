from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def showCatalog():
    return 'page to show catalog'


@app.route('/catalog/<string:category_name>/items')
def showCategory(category_name):
    return 'page to show category items'


@app.route('/catalog/<string:category_name>/<string:item_name>')
def showItem(category_name,item_name):
    return 'page to show item'


@app.route('/catalog/new')
def newItem():
    return 'page to create a new item'


@app.route('/catalog/<string:item_name>/edit')
def editItem(item_name):
    return 'page to edit an item'


@app.route('/catalog/<string:item_name>/delete')
def deleteItem(item_name):
    return 'page to delete an item'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
