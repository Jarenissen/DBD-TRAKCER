from enum import Enum

class Killer(Enum):
	NotSelected = 0
	Artist = 1
	Cannibal = 2
	Cenobite = 3
	Clown = 4
	DeathSlinger = 5
	Demogorgon = 6
	Executioner = 7
	GhostFace = 8
	Hillbilly = 9
	Huntress = 10
	Legion = 11
	MichaelMyers = 12
	Nemsis = 13
	SkullMerchant = 14
	Spirit = 15
	TheBlight = 16
	TheDoctor = 17
	TheDredge = 18
	TheGoodguy = 19
	TheHag = 20
	TheKnight = 21
	TheLich = 22
	TheMastermind = 23
	TheNightmare = 24
	TheNurse = 25
	TheOni = 26
	TheOnryo = 27
	ThePig = 28
	ThePlague = 29
	TheShape = 30
	TheSingularity = 31
	TheTrapper = 32
	TheTwins = 33
	TheUnknown = 34
	TheWraith = 35
	TheXenomorph = 36
	Trickster = 37

	def get_img_path(self):
		if self.value is not 0:
			return f"src/assets/killers/{self.name}.png"
		else: return None