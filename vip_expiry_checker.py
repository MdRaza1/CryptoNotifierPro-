# vip_expiry_checker.py

import json
import time

VIP_JSON_PATH = "vip_users.json"

def load_vip_data():
    try:
        with open(VIP_JSON_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_vip_data(data):
    with open(VIP_JSON_PATH, "w") as file:
        json.dump(data, file, indent=4)

def check_and_expire_vip():
    vip_data = load_vip_data()
    current_time = int(time.time())
    expired_users = []

    for user_id, info in list(vip_data.items()):
        if "expiry" in info and current_time > info["expiry"]:
            expired_users.append(user_id)
            del vip_data[user_id]

    if expired_users:
        print(f"⛔ VIP expired for: {', '.join(expired_users)}")
        save_vip_data(vip_data)
    else:
        print("✅ No expired VIPs.")

# OPTIONAL: Run on import (if desired)
if name == "main":
    check_and_expire_vip()
