from enum import Enum

class Map(Enum):
    NotSelected = 0
    GreenvilleSquare = 1
    
    def get_img_path(self):
        if self.value is not 0:
            return f"src/assets/maps/{self.name}.png"
        else: return None