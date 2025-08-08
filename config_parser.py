import json

def parse_file(filename="db_connection.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return None

if __name__=='__main__':
    print(parse_file())

