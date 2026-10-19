
import hashlib
from pathlib import Path


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()

    except OSError as error:
        print(f"Error reading file: {error}")
        return None


def main():
    file_path = input("Enter the file path: ").strip()
    path = Path(file_path)

    if not path.is_file():
        print("Error: File not found.")
        return

    original_hash = calculate_hash(path)

    if original_hash is None:
        return

    print("\nFile Integrity Report")
    print("-" * 35)
    print(f"File: {path.name}")
    print(f"SHA-256: {original_hash}")

    confirm = input("\nCheck the file again? (yes/no): ")

    if confirm.lower() == "yes":
        current_hash = calculate_hash(path)

        if current_hash is None:
            return

        if original_hash == current_hash:
            print("Status: File content is unchanged.")
        else:
            print("Status: File content has changed.")


if __name__ == "__main__":
    main()
