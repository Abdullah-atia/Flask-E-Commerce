from market import app
from market import db
import os

if __name__ == '__main__':
    # check if db file exists if not create it 
    if not os.path.exists(".market/market.db"):
        print("Database doesn't exist creating new one ...")
        db.init_app(app)
        with app.app_context():
            db.create_all()

    app.run(debug=True)