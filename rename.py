import os
import re

# Rename folders like:
# 1-two-sum -> 0001-two-sum
# 18-4sum -> 0018-4sum
# 181-employees -> 0181-employees

for item in os.listdir("."):
    if not os.path.isdir(item):
        continue

    # Skip hidden folders like .git and .github
    if item.startswith("."):
        continue

    match = re.match(r"^(\d+)-(.*)$", item)

    if not match:
        continue

    number = int(match.group(1))
    title = match.group(2)

    new_name = f"{number:04d}-{title}"

    if item != new_name:
        print(f"Renaming: {item} -> {new_name}")
        os.rename(item, new_name)
