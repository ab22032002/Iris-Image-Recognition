from database import load_db, save_db, hash_password

def register_admin(username, password):
    db = load_db()
    if db["admin"] is not None:
        raise PermissionError("Admin already registered.")
    db["admin"] = {
        "username": username,
        "password": hash_password(password)
    }
    save_db(db)
    print("Admin registered successfully.")

def add_user(user_id, features):
    db = load_db()
    if user_id in db["users"]:
        raise ValueError("User ID already exists.")
    db["users"][user_id] = {"features": features}
    save_db(db)
    print(f"User {user_id} added successfully.")

def update_user(user_id, features):
    db = load_db()
    if user_id not in db["users"]:
        raise ValueError("User ID does not exist.")
    db["users"][user_id]["features"] = features
    save_db(db)
    print(f"User {user_id} updated successfully.")
