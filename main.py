from models.create_csv.create_csv import csv_creator
from flask import Flask
app = Flask(__name__)


# step 1 calls /create_csv
@app.route('/')
def download_csv():  # main index page
    return create_csv()


@app.route('/create_csv')
# step 2 creates csv and downloads it
def create_csv():
    return csv_creator()


if __name__ == '__main__':
    app.run()
