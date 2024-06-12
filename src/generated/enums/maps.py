from enum import Enum

class Map(Enum):
	NotSelected = 0
	Azarov27sRestingPlace = 1
	BadhamPreschool = 2
	BloodLodge = 3
	CoalTower = 4
	DeadDawgSaloon = 5
	DisturbedWard = 6
	EyrieofCrows = 7
	FamilyResidence = 8
	FatherCampbell27sChapel = 9
	ForgottenRuins = 10
	FracturedCowshed = 11
	GardenofJoy = 12
	GasHeaven = 13
	GreenvilleSquare = 14
	GrimPantry = 15
	GroaningStorehouse = 16
	IronworksofMisery = 17
	LampkinLane = 18
	MidwichElementarySchool = 19
	Mother27sDwelling = 20
	MountOrmondResort = 21
	NostromoWreckage = 22
	RaccoonCityPoliceStation = 23
	RaccoonCityPoliceStationEastWing = 24
	RaccoonCityPoliceStationWestWing = 25
	RancidAbattoir = 26
	RottenFields = 27
	SanctumofWrath = 28
	ShelterWoods = 29
	SuffocationPit = 30
	TheGame = 31
	ThePaleRose = 32
	TheShatteredSquare = 33
	TheTempleofPurgation = 34
	TheThompsonHouse = 35
	TheUndergroundComplex = 36
	TobaLanding = 37
	TormentCreek = 38
	TreatmentTheatre = 39
	Wreckers27Yard = 40
	WretchedShop = 41

	def get_img_path(self):
		if self.value is not 0:
			return f"src/assets/maps/{self.name}.png"
		else: return None