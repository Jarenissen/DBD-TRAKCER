import sys
sys.path.append(".") 
from src.generated.enums.maps import Map
from src.generated.enums.killers import Killer
from src.generated.enums.realms import Realm
from src.generated.enums.survivors import Survivor

# can change
TYPE = Map

with open("out.py", "w+") as file:
    file.write(f"def get_{TYPE.__name__.lower()}_radio(self):\n    ")
    for item in TYPE:
        if item.value != 0:
            file.write(f"if self.{item.name.lower()}button.isChecked():\n        return {TYPE.__name__}.{item.name}\n    el")
    file.write(f"se:\n    \traise No{TYPE.__name__}Selected")