import pandas as pd
import json
import operator
import re
from datetime import datetime


def get_json_data():
    with open('./files/presidential.json') as file:
        data = json.load(file)

        # sorting on the basis of Name
        data.sort(key=operator.itemgetter('nm'))
        r = re.compile(r"(?:(?<=\s)|^)(?:[a-z]|\d+)", re.I)
        for m in data:
            m['nm'] = m['nm'].split(' ')[0][::-1]  # reverse first name after splitting full name
            m['pp'] = ''.join(r.findall(m['pp']))  # creating abbreviation for party
            m['tm'] = m['tm'][:4]  # extracting starting year of the term

        # arranging columns in the required format
        columns = ['nm', 'pp', 'tm', 'president']
        data_frame = pd.DataFrame(data, columns=columns)
        # excluding all parties with which have the word Federalist in their name
        data_frame = data_frame[data_frame.pp != 'Federalist']
        data_frame = data_frame[data_frame.pp != 'None, Federalist']
        new_names = {
            "nm": "Name",
            "pp": "Party",
            "tm": "Presidential term",
            "president": "President number"
        }
        data_frame = data_frame.rename(columns=new_names)

        # adding new column with timestamp
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_frame['Ingestion Time'] = time_stamp
        return data_frame
