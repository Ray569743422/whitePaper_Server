import pandas as pd
import json
import sys
import os
from datetime import datetime

'''
python xlsx2json.py data_file.xlsx
'''


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # if passed in object is datetime object
        # convert it to a string
        if isinstance(obj, datetime):
            return str(obj)
        # otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    df = pd.read_excel(sys.argv[1])
    df.fillna('-',inplace=True)
    df.drop_duplicates(inplace=True)
    print(df.head())
    # j = df.to_json('file.json', orient='records', lines=True)

    # el-table input data format
    d = df.to_dict('records')
    #j = json.dumps(d)

    fn = os.path.basename(sys.argv[1]).split('.')[0]
    with open(f'{fn}.json','w') as f:
        json.dump(d,f,cls=DTEncoder)


