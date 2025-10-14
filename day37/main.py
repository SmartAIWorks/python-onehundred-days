
import requests, datetime as dt


#https://pixe.la/v1/users/jmalab202501/graphs/udemy-2025-01.html
PIXELA_URL = 'https://pixe.la/v1'
PIXELA_USERS_URL = f'{PIXELA_URL}/users'
PIXELA_GRAPH_URL = f'{PIXELA_URL}/users/jmalab202501/graphs'
PIXELA_GRAPH_PIXEL_URL = f'{PIXELA_URL}/users/jmalab202501/graphs/udemy-2025-01'


headers = {
        'X-USER-TOKEN': 'token-123'
    }
def create_user():

    user_params = {
        "token": "token-123",
        "username": "jmalab202501",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"

    }
    response = requests.post(url=PIXELA_USERS_URL, json=user_params)
    response.raise_for_status()
    print(response.json())

def create_user_graph():
    data = {
        'id': 'udemy-2025-01',
        'name': 'Udemy Training',
        'unit': 'module',
        'type': 'int',
        'color': 'ajisai'

    }
 
    response = requests.post(url=PIXELA_GRAPH_URL, json=data, headers=headers)
    print(response.json())

def post_graph_pixel():
    post_date = dt.datetime.now() - dt.timedelta(days=2)
    data = {
        'date': post_date.strftime('%Y%m%d'),
        'quantity': '20'
    }

    response = requests.post(url=PIXELA_GRAPH_PIXEL_URL, json=data, headers=headers)

    print(response.json())

def main():

    # create_user()
    #create_user_graph()
    post_graph_pixel()

  

if __name__ == '__main__':
    main()