import os
import re

from flask import Flask
from flask_restful import Api

from resources.item import Item, ItemList

app = Flask(__name__)

app.config['DEBUG']=True

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DataBase_URL','sqlite:///data.db')

uri = os.getenv("DATABASE_URL")  # or other relevant config var
print(uri)
if uri == None:
    uri = "postgresql://"
else:
#uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(uri, 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    from models.db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
