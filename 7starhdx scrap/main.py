import requests

url = 'https://www.python.org'

response = requests.get(url)
# print(type(response))

# print(response.status_code)

# print(response.ok)

# print(response.content.decode())

print(response.encoding)

print(response.headers)