import argparse
import hashlib

def hash_convert(password, algorithm, salt=""):
    combined = salt + password
    if algorithm == "md5":
        return hashlib.md5(combined.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(combined.encode()).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(combined.encode()).hexdigest()
    else:
        raise ValueError("Unsupported algorithm")

parser = argparse.ArgumentParser(description="Hash a password using a selected algorithm and optional salt.")
parser.add_argument("-p", "--password", required=True, help="Password to hash")
parser.add_argument("-a", "--algorithm", required=True, choices=["md5", "sha256", "sha512"], help="Hash algorithm")
parser.add_argument("-s", "--salt", default="", help="Optional salt")

args = parser.parse_args()

hashed = hash_convert(args.password, args.algorithm.lower(), args.salt)
print(f"Hashed password: {hashed}")
