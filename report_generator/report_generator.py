import json
from datetime import datetime


def generate_for_object(obj, count_field_name, field_count, filename_beginning, fields={}):
    try:
        obj[count_field_name] = field_count

        if fields:
            for a in fields:
                obj[a] = fields[a]

        js = json.dumps(obj.__dict__)

        name = "{}_{}.json".format(filename_beginning, datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))

        with open("../reports/" + name,
                  "w") as f:
            f.write(str(js))
        return name
    except:
        return None
