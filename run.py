from app import app
from models.db import db

db.init_app(app)
#test
@app.before_first_request
def create_tables():
    db_create_all()
if __name__ == '__main__':
    app.run(port=5002, debug=True)
