import json
import traceback
from datetime import datetime

from other_classes.constants import REPORTS_DIRECTORY


def generate_for_object(obj1, count_field_name, field_count, filename_beginning, fields={}):
    try:
        obj = obj1.__dict__
        obj[count_field_name] = field_count

        fields_in_obj = list(obj.keys())

        for f in fields_in_obj:
            if "_id" in f:
                temp = obj[f]
                del obj[f]
                obj["db_" + f] = temp

        if fields:
            for a in fields:
                obj[a] = fields[a]

        js = json.dumps(obj)

        name = "{}_{}.json".format(filename_beginning, datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))

        with open(REPORTS_DIRECTORY + name,
                  "w") as f:
            f.write(str(js))
        return name
    except Exception as e:
        print(e)
        traceback.print_exc()

        return None
