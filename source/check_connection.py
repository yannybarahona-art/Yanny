import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    verify=False,
    timeout=10
)

print(response.status_code)
print(response.json())