import requests

params = {
    'amount': 11,
    'type': 'boolean',
    'category': 18
}
response = requests.get(url="https://opentdb.com/api.php", params=params)
response.raise_for_status()
question_data = response.json()['results']