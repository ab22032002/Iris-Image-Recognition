import argparse
from utils import validate_image
from database import load_db, save_db, check_admin
from features import extract_features
from matcher import match_xor
import admin

def main():
    parser = argparse.ArgumentParser(description="Iris Recognition System")
    parser.add_argument("--register-admin", action="store_true")
    parser.add_argument("--add", action="store_true")
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--match", action="store_true")
    parser.add_argument("--user-id", type=str, help="User ID")
    parser.add_argument("--username", type=str, help="Admin username")
    parser.add_argument("--password", type=str, help="Admin password")
    parser.add_argument("--image", type=str, help="Path to iris image")
    args = parser.parse_args()

    db = load_db()

    if args.register_admin:
        if args.username and args.password:
            admin.register_admin(args.username, args.password)
        else:
            print("Provide --username and --password")
        return

    if args.add or args.update:
        if not check_admin(db, args.username, args.password):
            print("Invalid admin credentials.")
            return
        if not args.user_id or not args.image:
            print("Provide --user-id and --image")
            return
        img = validate_image(args.image)
        features = extract_features(img)
        if args.add:
            admin.add_user(args.user_id, features)
        else:
            admin.update_user(args.user_id, features)
        return

    if args.match:
        if not args.image:
            print("Provide --image")
            return
        img = validate_image(args.image)
        features = extract_features(img)
        matched_id, distance = match_xor(features, db)
        if matched_id:
            print(f"Matched with {matched_id}, XOR Distance: {distance}")
        else:
            print("No match found.")

if __name__ == "__main__":
    main()
