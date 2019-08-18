from models.json_data.json_data import get_json_data
from flask import make_response


def csv_creator():
    # getting json data
    data_frame = get_json_data()
    resp = make_response(data_frame.to_csv(index=False))
    # creating csv
    resp.headers["Content-Disposition"] = "attachment; filename=presidential.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
