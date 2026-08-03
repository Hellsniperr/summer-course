import requests
# address = "https://jsonplaceholder.typicode.com"
# response = requests.get(address)

# # print(response)

# print(response.elapsed)

# # 2

# response = requests.get(f'{address}/posts/1')

# response.status_code
# response.reason
# response.raw
# response.json()
# type(rresponse)
# response.elapsed
# dir(response)
# response.headers
# response.headers['Content-Type']

# HO 2 

address = "https://httpbin.org"


url = "- `https://httpbin.org/basic-auth/student/pass123"
credentials = {"user": "psswd"}

response = requests.get(url, auth=("student", "pass123"), json=credentials)


