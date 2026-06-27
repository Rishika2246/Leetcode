import os
import re
import shutil

PADDING = 4

print("=== Starting rename.py ===")

for item in sorted(os.listdir(".")):
    if not os.path.isdir(item):
        continue

    # Skip hidden/system folders
    if item.startswith("."):
        continue

    match = re.match(r"^(\d+)-(.*)$", item)
    if not match:
        continue

    number = int(match.group(1))
    title = match.group(2)

    new_name = f"{number:0{PADDING}d}-{title}"

    # Already padded correctly
    if item == new_name:
        continue

    print(f"\nProcessing: {item}")

    # If padded folder already exists, merge and delete old folder
    if os.path.exists(new_name):
        print(f"Destination exists: {new_name}")
        print("Merging...")

        for root, dirs, files in os.walk(item):
            rel = os.path.relpath(root, item)

            if rel == ".":
                dest_root = new_name
            else:
                dest_root = os.path.join(new_name, rel)

            os.makedirs(dest_root, exist_ok=True)

            for file in files:
                src = os.path.join(root, file)
                dst = os.path.join(dest_root, file)

                if not os.path.exists(dst):
                    shutil.move(src, dst)
                    print(f"Moved: {src} -> {dst}")
                else:
                    print(f"Skipped existing: {dst}")

        shutil.rmtree(item)
        print(f"Deleted duplicate folder: {item}")

    else:
        print(f"Renaming {item} -> {new_name}")
        os.rename(item, new_name)

print("\n=== Finished ===")
