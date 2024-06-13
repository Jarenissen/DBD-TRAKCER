from pathlib import Path
import os

# Can change

IMAGE_PATH = "maps/"
ENUM_NAME = "Map"
DEST_NAME = "Maps.py"

# Dont change

DEST_PATH = "src/generated/enums/"
FULL_PATH = "src/assets/" + IMAGE_PATH

Path(DEST_PATH).mkdir(parents=True, exist_ok=True)
with open(DEST_PATH+DEST_NAME, "w+") as enum_file:
    enum_file.write(f"from enum import Enum\nfrom tracker.util.pathing import asset_path\n\nclass {ENUM_NAME}(Enum):\n\tNotSelected = 0\n")
    num = 1
    for file in os.listdir(FULL_PATH):
        name = os.fsdecode(file)
        if name.endswith(".png"):
            item_name = Path(name).stem.replace("_", "").replace("%27", "").replace("%", "").replace("'", "").replace("é", "e")
            os.rename(FULL_PATH+name, FULL_PATH+item_name+".png")
            enum_file.write(f"\t{item_name} = {num}\n")
            num += 1

    enum_file.write(f"\n\tdef get_img_path(self):\n\t\tif self.value is not 0:\n\t\t\treturn asset_path(f\"{IMAGE_PATH}" + "{self.name}.png\")\n\t\telse: return None")