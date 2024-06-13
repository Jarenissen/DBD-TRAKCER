from enum import Enum
from tracker.util.pathing import asset_path

class Survivor(Enum):
	NotSelected = 0
	Ace = 1
	Ada = 2
	Adam = 3
	Alan = 4
	Ash = 5
	Bill = 6
	Cheryl = 7
	Claudette = 8
	David = 9
	DavidTapp = 10
	DwightFairfield = 11
	Ellen = 12
	Elodie = 13
	Felix = 14
	Feng = 15
	Gabriel = 16
	Haddie = 17
	Jake = 18
	Jane = 19
	Jeff = 20
	Jill = 21
	Jonah = 22
	Kate = 23
	laurie = 24
	Leon = 25
	MegThomas = 26
	Mikaela = 27
	Nancy = 28
	Nea = 29
	Nicolas = 30
	Quentin = 31
	Rebecca = 32
	Renato = 33
	Sable = 34
	Steve = 35
	Thalita = 36
	Troupe = 37
	Vittorio = 38
	Yoichi = 39
	Yui = 40
	Yun = 41
	Zarina = 42

	def get_img_path(self):
		if self.value is not 0:
			return asset_path(f"survivors/{self.name}.png")
		else: return None