import requests

myobj = {'item': 'banana'}
x = requests.post('http://127.0.0.1:8000/polls/answer_request/34', json=myobj)

print(x.text)
