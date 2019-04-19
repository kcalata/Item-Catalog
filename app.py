#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db',
connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).all()
    items = session.query(Item).order_by(Item.id.desc())
    return render_template('catalog.html', categories=categories, items=items)


@app.route('/catalog/<string:category_name>/items')
def showCategory(category_name):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category_name=category.name)
    return render_template('category.html', categories=categories, category=category, items=items)


@app.route('/catalog/<string:category_name>/<string:item_name>')
def showItem(category_name,item_name):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(category_name=category.name).filter_by(name=item_name).one()
    return render_template('item.html', categories=categories, item=item)


@app.route('/catalog/new', methods=['GET', 'POST'])
def newItem():
    categories = session.query(Category).all()
    if request.method == 'POST':
        newItem = Item(name=request.form['dessert'], description=request.form['description'], category_name=request.form['category'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newItem.html', categories=categories)


@app.route('/catalog/<string:item_name>/edit', methods=['GET', 'POST'])
def editItem(item_name):
    categories = session.query(Category).all()
    editedItem = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        if request.form['dessert']:
            editedItem.name = request.form['dessert']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['category']:
            editedItem.category_name = request.form['category']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('editItem.html',item=editedItem, categories=categories)


@app.route('/catalog/<string:item_name>/delete', methods=['GET', 'POST'])
def deleteItem(item_name):
    deletedItem = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('deleteItem.html', item=deletedItem)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
