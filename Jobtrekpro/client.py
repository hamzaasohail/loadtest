import requests
import random
import time
from datetime import datetime, timedelta


# === CONFIGURATION ===
API_URL = "https://api.jobtrekpro.com/api/clients"
ADMIN_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJlOWIwNDk0Ny05MTdmLTQ1YzQtYWQ3NS1jNjQxZjZhZDAwMmQiLCJlbWFpbCI6Im1hcmtAeW9wbWFpbC5jb20iLCJyb2xlIjoib3duZXIiLCJpYXQiOjE3NjQzMjIzOTMsImV4cCI6MTc2NDQwODc5M30.z5hew4x8y_KYYAMSh-OcGMdBJS9nC7SMHvqBD2dV3JE"
BASE_EMAIL = "mark@yopmail.com"

headers = {
    "Authorization": f"Bearer {ADMIN_TOKEN}",
    "Content-Type": "application/json"
}


# === HELPERS ===

def pick(arr):
    return random.choice(arr)


# === DATA POOLS ===

FIRST = [
    'John', 'Michael', 'David', 'James', 'Robert', 'William',
    'Sarah', 'Jennifer', 'Lisa', 'Mary', 'Patricia', 'Linda',
    'Ahmed', 'Ali', 'Hassan', 'Fatima', 'Aisha', 'Zainab',
    'Chris', 'Daniel', 'Matthew', 'Emma', 'Olivia', 'Sophia',
    'Illana', 'Carlos', 'Marcus', 'Elena', 'Diego', 'Isabella',
    'Alex'
]

LAST = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia',
    'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez',
    'Khan', 'Ahmed', 'Ali', 'Hassan', 'Malik', 'Shah',
    'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson',
    'Dickson', 'Cooper', 'Bennett', 'Foster', 'Coleman'
]

ADDRESSES = [
    "123 Main Street", "456 Oak Avenue", "789 Elm Boulevard",
    "321 Pine Road", "654 Maple Drive", "987 Cedar Lane",
    "147 Birch Street", "258 Willow Way", "369 Aspen Court",
    "741 Spruce Avenue", "saint andrew"
]

AVAILABLE_TAG_IDS = [
    "f2bdc5c8-c13c-4b3e-9c1a-c50afee0018c",
    "a89f1c52-71a6-44f3-b094-76a8dee7b736",
    "56d0afea-8181-449c-b30f-f5c810fd8492",
    "1c9c4aad-35ee-40f1-86ad-ac711c46dc4b",
    "1fafdbf6-a4a3-4907-9142-efb033eb14c5",
    "844269f9-6e02-411b-b06c-fd0a7697282e",
    "9d245945-dfab-457e-9fa2-b2d5301400c4"
]


# === NEW PAYLOAD GENERATOR ===

def generate_client(i):
    # Name & email
    first = pick(FIRST)
    last = pick(LAST)
    name = f"{first} {last}"

    base, domain = BASE_EMAIL.split("@")
    email = f"{base}+{i}@{domain}"

    # Phone
    phone = f"+1 ({random.randint(100, 999)}) {random.randint(1000000, 9999999)}"

    # Address
    address = pick(ADDRESSES)

    # tagIds → string array
    tagIds = [pick(AVAILABLE_TAG_IDS)]

    # FINAL PAYLOAD (matches your request)
    payload = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "tagIds": tagIds
    }

    return payload


# === CREATE CLIENTS ===

def create_clients(n=150):
    success, fail = 0, 0

    for i in range(1, n + 1):
        payload = generate_client(i)

        try:
            response = requests.post(
                API_URL, json=payload, headers=headers, timeout=10)

            if response.status_code in (200, 201):
                success += 1
                print(f"[{i}] Created: {payload['email']}")
            else:
                fail += 1
                print(f"[{i}] ❌ Failed ({response.status_code}): {response.text}")

        except Exception as e:
            fail += 1
            print(f"[{i}] ⚠️ Exception: {e}")

        time.sleep(0.1)

    print(f"\n✔ Success: {success} | ❌ Failed: {fail}")


if __name__ == "__main__":
    create_clients(150)
