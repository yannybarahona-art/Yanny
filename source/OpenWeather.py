import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main() -> None:
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10)
        # Raise an exception for 4xx/5xx responses
        response.raise_for_status()
        users = response.json()
        print(f"Retrieved {len(users)} users:\n")
        for user in users:
            print(
                f"ID: {user['id']}, "
                f"Name: {user['name']}, "
                f"Email: {user['email']}"
            )
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
if __name__ == "__main__":
    main()