import json


def parse_json(path):
    f = open(f'app/{path}')
    data = json.load(f)
    f.close()
    return data