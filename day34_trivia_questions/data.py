# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "AMD created the first consumer 64-bit processor.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "'HTML' stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]


import requests, html
from typing import List, Dict, Any, Union


def decode_entities(obj: Union[str, list, dict, Any]) -> Union[str, list, dict, Any]:
    if isinstance(obj, str):
        return html.unescape(obj)
    elif isinstance(obj, list):
        return [decode_entities(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: decode_entities(v) for k, v in obj.items()}
    return obj

def fetch_data() -> List[Dict[str, Any]]:

    parameters = {
        'amount': 10,
        'type': 'boolean'
    }
    response = requests.get('https://opentdb.com/api.php', params=parameters)
    response.raise_for_status()

    parsed_data = response.json()['results']

    #return parsed_data
    decoded_data = decode_entities(parsed_data)
    # Type assertion to help the linter understand the return type
    return decoded_data  # type: ignore


def main():
    pass

if __name__ =='__main__':
    main()