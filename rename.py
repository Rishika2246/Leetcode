import os
import re

PADDING = 4

for item in os.listdir("."):
    if not os.path.isdir(item):
        continue

    # Skip hidden folders
    if item.startswith("."):
        continue

    match = re.match(r"^(\d+)-(.*)$", item)

    if not match:
        continue

    number = int(match.group(1))
    title = match.group(2)

    new_name = f"{number:0{PADDING}d}-{title}"

    if item != new_name:
        print(f"{item} -> {new_name}")
        os.rename(item, new_name)
