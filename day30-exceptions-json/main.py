
import json

from tkinter import messagebox


def read_json(file):
    with open(file, 'r') as data:
        return json.load(data)
def save_to_json(data: dict):
    with open('data.json', 'w') as j:
        json.dump(data, j)


data = {"name" : "john", "hobbies": ['play mobile', 'basketball', 'play chess']}



save_to_json(data)
content = read_json('data.json')
messagebox.showinfo('Hi', content)
# try:
#     with open('data.txt') as f:
#         f.read()

# except Exception as e:
#     print(e)
# else:
#     pass
# finally:
#     pass