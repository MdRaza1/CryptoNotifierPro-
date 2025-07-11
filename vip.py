# vip.py
import json
import os
from datetime import datetime, timedelta

VIP_FILE = "vip_members.json"

def load_vip():
    if not os.path.exists(VIP_FILE):
        with open(VIP_FILE, "w") as f:
            json.dump({}, f)
    with open(VIP_FILE, "r") as f:
        return json.load(f)

def save_vip(data):
    with open(VIP_FILE, "w") as f:
        json.dump(data, f, indent=4)

def is_user_vip(user_id):
    data = load_vip()
    user = str(user_id)
    if user in data:
        expiry = datetime.strptime(data[user], "%Y-%m-%d")
        if expiry >= datetime.today():
            return True
    return False

def add_vip(user_id, days):
    data = load_vip()
    expiry = datetime.today() + timedelta(days=days)
    data[str(user_id)] = expiry.strftime("%Y-%m-%d")
    save_vip(data)
    return expiry.strftime("%d %b %Y")

def remove_vip(user_id):
    data = load_vip()
    if str(user_id) in data:
        del data[str(user_id)]
        save_vip(data)
        return True
    return False

def get_all_vips():
    return load_vip()
