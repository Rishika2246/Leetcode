import os
import re

for folder in os.listdir("."):

    if not os.path.isdir(folder):
        continue

    match = re.match(r"^(\d+)-(.*)", folder)

    if not match:
        continue

    number = int(match.group(1))
    title = match.group(2)

    new_name = f"{number:04d}-{title}"

    if folder != new_name:
        print(f"{folder} -> {new_name}")
        os.rename(folder, new_name)
