import json

def main():
    data = {

        'username': 'Booty',
        'active': True,
        'honey_hours': 10,
        'id': 125569997,

    }

    data2 = {

        'username': 'Jerbear',
        'active': True,
        'honey_hours': 4,
        'id': 836219543,

    }

    s = json.dumps(data)
    return s