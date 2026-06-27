import os
import re
import shutil

PADDING = 4

print("=== Starting rename.py ===")

for item in os.listdir("."):
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

    # Already correctly named
    if item == new_name:
        continue

    # Destination already exists
    if os.path.exists(new_name):
        print(f"Merging {item} -> {new_name}")

        for root, dirs, files in os.walk(item):
            rel_path = os.path.relpath(root, item)
            dest_root = os.path.join(new_name, rel_path)

            os.makedirs(dest_root, exist_ok=True)

            for file in files:
                src = os.path.join(root, file)
                dst = os.path.join(dest_root, file)

                if not os.path.exists(dst):
                    shutil.move(src, dst)
                    print(f"  Moved {src} -> {dst}")
                else:
                    print(f"  Skipped existing file: {dst}")

        shutil.rmtree(item)
        print(f"Deleted duplicate folder: {item}")

    else:
        print(f"Renaming {item} -> {new_name}")
        os.rename(item, new_name)

print("=== Done ===")
