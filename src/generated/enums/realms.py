from enum import Enum
from tracker.util.pathing import asset_path

class Realm(Enum):
	NotSelected = 0
	AutohavenWreckers = 1
	BackwaterSwamp = 2
	ColdwindFarm = 3
	CrotusPrennAsylum = 4
	DvarkaDeepwood = 5
	ForsakenBoneyard = 6
	GideonMeatPlant = 7
	GraveofGlenvale = 8
	Haddonfield = 9
	HawkinsNationalLaboratory = 10
	LerysMemorialInstitute = 11
	Ormond = 12
	RaccoonCity = 13
	RedForest = 14
	SilentHill = 15
	Springwood = 16
	TheDecimatedBorgo = 17
	TheMacMillanEstate = 18
	WitheredIsle = 19
	YamaokaEstate = 20

	def get_img_path(self):
		if self.value is not 0:
			return asset_path(f"realms/{self.name}.png")
		else: return None