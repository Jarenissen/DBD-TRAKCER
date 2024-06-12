from pathlib import Path
import os

# Can change

IMAGE_PATH = "src/assets/survivors/"
ENUM_NAME = "Survivor"
DEST_NAME = "survivors.py"

# Dont change

DEST_PATH = "src/generated/enums/"

Path(DEST_PATH).mkdir(parents=True, exist_ok=True)
with open(DEST_PATH+DEST_NAME, "w+") as enum_file:
    enum_file.write(f"from enum import Enum\n\nclass {ENUM_NAME}(Enum):\n\tNotSelected = 0\n")
    num = 1
    for file in os.listdir(IMAGE_PATH):
        name = os.fsdecode(file)
        if name.endswith(".png"):
            item_name = Path(name).stem.replace("_", "").replace("%", "").replace("'", "").replace("é", "e")
            os.rename(IMAGE_PATH+name, IMAGE_PATH+item_name+".png")
            enum_file.write(f"\t{item_name} = {num}\n")
            num += 1

    enum_file.write(f"\n\tdef get_img_path(self):\n\t\tif self.value is not 0:\n\t\t\treturn f\"{IMAGE_PATH}" + "{self.name}.png\"\n\t\telse: return None")