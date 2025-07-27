import getpass
import hashlib
import os

def get_stored_password_hash():
    salt = b'\x12\x34\x56\x78\x9a\xbc\xde\xf0\x12\x34\x56\x78\x9a\xbc\xde\xf0'
    stored_hash = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3c8c8f68573e6b5d7b2d8e8d1"
    return stored_hash, salt

def authenticate_user():
    username = input("Enter your username: ").strip()
    print("Hello,", username)
    
    if username.lower() == "admin":
        password = getpass.getpass("Enter your password: ")
        stored_hash, salt = get_stored_password_hash()
        password_hash = hashlib.sha256(salt + password.encode()).hexdigest()
        
        if password_hash == stored_hash:
            print("✅ Access granted.")
        else:
            print("❌ Access denied: Incorrect password.")
    else:
        print("🔒 Access restricted to admin users only.")

if __name__ == "__main__":
    authenticate_user()
