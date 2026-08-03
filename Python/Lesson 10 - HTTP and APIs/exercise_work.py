import requests
address = "https://jsonplaceholder.typicode.com"
r = requests.get(address)

# print(r)

print(r.elapsed)

# 2

r = requests.get(f'{address}/posts/1')

r.status_code
r.reason
r.raw
r.json()
type(r)
r.elapsed
dir(r)
r.headers
r.headers['Content-Type']

#3  

r.content
r.headers

