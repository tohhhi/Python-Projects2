import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '+40755621608',
  'message': 'Salut Marian ce faci?',
  'key': 'textbelt',
})
print(resp.json())