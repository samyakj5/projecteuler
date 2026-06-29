from pathlib import Path

import re

folder = Path(".")  # current directory

for file in folder.glob("problem*.py"):

    match = re.fullmatch(r"problem(\d+)\.py", file.name)

    if match:

        num = int(match.group(1))

        new_name = f"problem{num:04d}.py"

        file.rename(folder / new_name)

        print(f"{file.name} -> {new_name}")