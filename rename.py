import os
import re

print("Current directory:", os.getcwd())
print("Contents:")

for item in os.listdir("."):
    print("-", item)

print("\nRenaming...")

for item in os.listdir("."):
    if not os.path.isdir(item):
        continue

    if item.startswith("."):
        continue

    match = re.match(r"^(\d+)-(.*)$", item)

    if not match:
        continue

    number = int(match.group(1))
    title = match.group(2)

    new_name = f"{number:04d}-{title}"

    print(f"{item} -> {new_name}")

    if item != new_name:
        os.rename(item, new_name)

print("Done.")
