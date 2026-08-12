# Problem 1

def recursive_squares(n):

    if n == 0:
        return []

    else:
        return recursive_squares(n - 1) + [n ** 2] #[n ** 2] is for the current call AND trip the base case; (n - 1) sets up the next call to the function

n = int(input("Enter a non-negative integer: "))
print(recursive_squares(n))


def palindrome_checker(s):

    s = s.lower()
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome_checker(s[1:-1])

def length(lst):
    if lst == []:
        return 0
    else:
        return length(lst[1:]) + 1

#challenge

def flatten(fat_lst):
    result = []

    for item in fat_lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# Problem 2

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def count_ways(n):
    if n < 0:
        return 1
    elif n == 0:
        return 1
    else:
        return count_ways(n - 1) + count_ways(n - 2)



def grid_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return grid_paths(m - 1, n) + grid_paths(m, n - 1)


# Problem 3

import requests


def get_user(user_id: int)-> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return {}

def create_user(name: str, job: str) -> dict:
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.post(url, json={"name": name, "job": job})
    if r.status_code != 201:
        return {}
    return r.json()

def update_user(user_id: int, name: str, job: str) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    r = requests.put(url, json={"name": name, "job": job})
    if r.status_code != 200:
        return {}
    return r.json()

def delete_user(user_id: int) -> bool:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    r = requests.delete(url)
    return r.status_code == 200

def get_users_page(page:int) -> list:
    url = f"https://jsonplaceholder.typicode.com/users?page={page}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json().get("data", [])
    return []

def partial_update_user(user_id: int, updates: dict) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    r = requests.patch(url, json=updates)
    if r.status_code != 200:
        return {}
    return {}



# Problem 4

def search_movie(api_key: str, query: str) -> dict:
    url = "https://api.themoviedb.org/3/search/movie"
    r = requests.get(url, params={"api_key": api_key, "query": query})
    if r.status_code != 200:
        return {}

    results = r.json().get("results", [])
    if not results:
        return {}
    return results[0]


def get_github_user(token: str, username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return {}
    return r.json()

def create_gist(token: str, description: str, filename: str, content: str) -> dict:
    url = "https://api.github.com/gists"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "description": description,
        "public": True,
        "files": {
            filename: {"content": content}
        },
    }
    r = requests.post(url, headers=headers, json=body)
    if r.status_code != 201:
        return ""   
    return str(r.json()["id"])


def delete_gist(token: str, gist_id: str) -> bool:
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.delete(url, headers=headers)
    return r.status_code == 204
    


if __name__ == "__main__":