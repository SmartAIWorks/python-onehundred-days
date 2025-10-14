
import requests, datetime as dt, os
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY  = os.getenv('NUTRITIONIX_API_KEY')
NUTRITIONIX_URL = os.getenv('NUTRITIONIX_URL')
NUTRITIONIX_NATURAL_EXERCISE_ENDPOINT = f'{NUTRITIONIX_URL}/{os.getenv('NUTRITIONIX_NATURAL_EXERCISE_ENDPOINT')}'

SHEETY_URL = os.getenv('SHEETY_URL', '')
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

class ExeciseStats:
    def __init__(self, execise:str, calories:float, duration: int):
        now = dt.datetime.now()
        self.date = now.strftime('%d/%m/%Y')
        self.time = now.strftime('%H:%M:%S')
        self.name = execise
        self.calories = calories
        self.duration = duration


def record(stats: ExeciseStats):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': SHEETY_AUTH
    }

    body = {
        'workout': {
            'date': stats.date,
            'time': stats.time,
            'exercise': stats.name,
            'duration': stats.duration,
            'calories': stats.calories
        }

    }

    response = requests.post(SHEETY_URL, json=body, headers=headers)
    print(response.json())
    response.raise_for_status()
 

    
def get_exercise_stats(query):
    headers = {
        'Content-Type' : 'application/json',
        'x-app-id': NUTRITIONIX_APP_ID,
        'x-app-key': NUTRITIONIX_API_KEY
    }

    body =  {
        'query': query
    }
    response = requests.post(NUTRITIONIX_NATURAL_EXERCISE_ENDPOINT, headers=headers, json=body)
    
    response.raise_for_status()

    print('>>>', response.json().get('exercises', []))

    if len(response.json().get('exercises', [])) == 0:
        raise ValueError('Something went wrong. Please try again later.')

    else:
        stats = response.json().get('exercises', {})
        print(stats)
        calories =  stats[0]['nf_calories']
        exercise_name =  stats[0]['name'].title()
        duration_min =  stats[0]['duration_min']

    return  ExeciseStats(calories=calories, execise=exercise_name, duration=duration_min)


def main():
    exercise = input('Tell me which execise you did? :')
    stats = get_exercise_stats(exercise)
    record(stats)

if __name__ == '__main__':
    main()