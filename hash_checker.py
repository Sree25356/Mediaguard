import hashlib
import sys

def get_file_hash(path):
    try:
        with open(path, 'rb') as file:
            data = file.read()
            sha256 = hashlib.sha256(data).hexdigest()
            print(f"✅ SHA256 hash of '{path}':\n{sha256}")
    except Exception as e:
        print(f"❌ Error reading file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hash_checker.py <file_path>")
    else:
        get_file_hash(sys.argv[1])
