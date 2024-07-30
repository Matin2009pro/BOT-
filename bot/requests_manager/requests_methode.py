from requests import get, post, put
from requests.exceptions import ConnectionError



#get url and data and send to server ,return true or false
def post_license(url:str, data):
    try:
        response = post(url=url, data=data)
        if response.status_code == 201 or response.status_code == 200:
            return True
    except ConnectionError:
        return False
    return False



#get url and data file and send to server ,return true or false
def post_file(url:str, data, file:dict):
    try:
        response = post(url=url, data=data, files=file)
        if response.status_code == 201 or response.status_code == 200:
            return response
    except ConnectionError:
        return False
    return False



#get url and data and send to server ,return json or false
def get_json(url:str, data):
    try:
        response = get(url=url, data=data)
        if response.status_code == 201:
            return response.json()
    except ConnectionError:
        return False
    return False