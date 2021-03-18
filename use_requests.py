import requests

url = 'https://detik.com'

try:
    res = requests.get(url)
    if res.status_code == 200:
        print(f'Success response = {res.status_code}\n')
        print(f'Content: \n{res.text}')
except Exception as e:
    print('Error ', e)
