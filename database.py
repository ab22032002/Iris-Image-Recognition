import json
import os
import hashlib

DB_FILE = "db.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"admin": None, "users": {}}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_admin(db, username, password):
    if db["admin"] is None:
        return False
    return (db["admin"]["username"] == username and 
            db["admin"]["password"] == hash_password(password))
