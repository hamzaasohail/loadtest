import requests
import random
import time

# === CONFIGURATION ===
# ← replace with your API endpoint
API_URL = "https://api.jobtrekpro.com/api/contractors"
ADMIN_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzMDkxOWZmOS0yNTQ0LTQ4NGMtOWFmOS04NTg5MzM2ZjIwNzgiLCJlbWFpbCI6IjEzbm92QHlvcG1haWwuY29tIiwicm9sZSI6Im93bmVyIiwiaWF0IjoxNzYyOTUxNDc0LCJleHAiOjE3NjMwMzc4NzR9.OP2UCBL4xAMgob0kX3gcW0iXH3Zi0JwMP4JPHeUwEEg"              # ← replace with your real admin token
# ← base inbox (check on yopmail.com/?testuser)
BASE_EMAIL = "random@yopmail.com"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzMDkxOWZmOS0yNTQ0LTQ4NGMtOWFmOS04NTg5MzM2ZjIwNzgiLCJlbWFpbCI6IjEzbm92QHlvcG1haWwuY29tIiwicm9sZSI6Im93bmVyIiwiaWF0IjoxNzYyOTUxNDc0LCJleHAiOjE3NjMwMzc4NzR9.OP2UCBL4xAMgob0kX3gcW0iXH3Zi0JwMP4JPHeUwEEg",
    "Content-Type": "application/json"
}


first_names = ["Chelsea", "Alex", "Jordan",
               "Taylor", "Morgan", "Casey", "Riley", "Jamie"]
last_names = ["Barber", "Smith", "Johnson", "Lee", "Brown", "Clark", "Adams"]


# 🧰 Add your possible specializations here
specializations_list = ["garage", "plumbing", "electrical", "hvac",
                        "landscaping", "carpentry", "painting", "roofing", "cleaning"]


def generate_contractor(i):
    first = random.choice(first_names)
    last = random.choice(last_names)
    # Select only 1 random specialization
    specialization = random.choice(specializations_list)
    specializations = [specialization]

    # YOPmail unique alias — all deliver to same inbox
    base_name = BASE_EMAIL.split("@")[0]
    domain = BASE_EMAIL.split("@")[1]
    email = f"{base_name}+{i}@{domain}"

    payload = {
        "firstName": first,
        "lastName": last,
        "email": email,
        "dateOfBirth": "1995-06-30",
        "phone": f"+1 (800) {random.randint(1000000, 9999999)}",
        "homeBaseAddress": "Voluptatem Dignissi",
        "hourlyRate": 10,
        "serviceRadius": 25,
        "skillLevel": "beginner",
        # 🎯 Random specializations
        "specializations": specializations,
        "status": "pending",
        "tags": [{"name": "urgent", "color": "#0055ff"}],
        "hasVehicle": False,
        "ownsTools": False,
        "yearsExperience": 10,
        "serviceAreas": [],
        "emergencyContactName": None,
        "emergencyContactPhone": None,
        "insuranceProvider": None,
        "licenseNumber": None,
        "licenseState": None,
        "vehicleType": None
    }

    return payload


def create_contractors(n=500):
    success, fail = 0, 0
    for i in range(1, n + 1):
        payload = generate_contractor(i)
        try:
            response = requests.post(
                API_URL, json=payload, headers=headers, timeout=10)
            if response.status_code in [200, 201]:
                success += 1
                print(f"[{i}] ✅ Created contractor: {payload['email']}")
            else:
                fail += 1
                print(f"[{i}] ❌ Failed ({response.status_code}): {response.text}")
        except Exception as e:
            fail += 1
            print(f"[{i}] ⚠️ Exception: {e}")

        # Optional: prevent backend rate-limiting
        time.sleep(0.1)

    print(f"\n✅ Success: {success} | ❌ Failed: {fail}")


if __name__ == "__main__":
    create_contractors(3)
