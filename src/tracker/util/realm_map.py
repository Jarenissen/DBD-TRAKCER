from generated.enums.maps import Map
from generated.enums.realms import Realm


MAPPER = {
        Realm.AutohavenWreckers: [
            Map.Azarov27sRestingPlace,
            Map.BloodLodge,
            Map.GasHeaven,
            Map.Wreckers27Yard,
            Map.WretchedShop,
        ],
        Realm.BackwaterSwamp: [
            Map.ThePaleRose,
            Map.GrimPantry,
        ],
        Realm.LerysMemorialInstitute: [
            Map.TreatmentTheatre,
        ],
        Realm.TheMacMillanEstate: [
            Map.CoalTower,
            Map.GroaningStorehouse,
            Map.IronworksofMisery,
            Map.ShelterWoods,
            Map.SuffocationPit
        ],
        Realm.ColdwindFarm: [
            Map.FracturedCowshed,
            Map.RancidAbattoir,
            Map.RottenFields,
            Map.TheThompsonHouse,
            Map.TormentCreek
        ],
        Realm.CrotusPrennAsylum: [
            Map.DisturbedWard,
            Map.FatherCampbell27sChapel,
        ],
        Realm.Haddonfield: [
            Map.LampkinLane,
        ],
        Realm.RedForest: [
            Map.Mother27sDwelling,
            Map.TheTempleofPurgation,
        ],
        Realm.Springwood: [
            Map.BadhamPreschool,
        ],
        Realm.GideonMeatPlant: [
            Map.TheGame,
        ],
        Realm.YamaokaEstate: [
            Map.FamilyResidence,
            Map.SanctumofWrath,
        ],
        Realm.Ormond: [
            Map.MountOrmondResort,
        ],
        Realm.HawkinsNationalLaboratory: [
            Map.TheUndergroundComplex,
        ],
        Realm.GraveofGlenvale: [
            Map.DeadDawgSaloon,
        ],
        Realm.SilentHill: [
            Map.MidwichElementarySchool,
        ],
        Realm.RaccoonCity: [
            Map.RaccoonCityPoliceStation,
            Map.RaccoonCityPoliceStationEastWing,
            Map.RaccoonCityPoliceStationWestWing,
        ],
        Realm.ForsakenBoneyard: [
            Map.EyrieofCrows,
        ],
        Realm.WitheredIsle: [
            Map.GardenofJoy,
            Map.GreenvilleSquare,
        ],
        Realm.TheDecimatedBorgo: [
            Map.TheShatteredSquare,
            Map.ForgottenRuins,
        ],
        Realm.DvarkaDeepwood: [
            Map.TobaLanding,
            Map.NostromoWreckage,
        ],

    }

def maps_from_realm(realm):
    return MAPPER[realm]