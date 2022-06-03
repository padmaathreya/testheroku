from app import app
from models.db import

db.init_app(app)
#test
@app.before_first_request
def create_tables():
    db_create_all()
