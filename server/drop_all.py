from app import create_app, db
import sys

y = input("\n Delete all data in DB ? (yes/no) (no-default) > ")

if y.lower() != "yes":
    sys.exit()

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    print("\n Every thing was deleted")
    print("\n sedn a request to 'http://127.0.0.1:1001/get_all_db_data' \n And see if there is any data")