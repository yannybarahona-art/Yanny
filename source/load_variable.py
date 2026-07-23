import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / ".env"

print(f"Looking for .env at: {env_path}")
print(f"File exists: {env_path.exists()}")

load_dotenv(env_path)

client_secret = os.getenv("CLIENT_SECRET")
token = os.getenv("TOKEN")

print("Secret "+ client_secret)
print("Tokent"+ token)