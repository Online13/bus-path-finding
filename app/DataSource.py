import random


class DataSource:
    def __init__(self) -> None:
        random.seed(5)

        self.BUS = {
            "B": [
                "Ambohitrimanjaka",
                "Tetezana",
                "Art_Malagasy",
                "Score_digue",
                "Andohatapenaka",
                "_67_Ha",
            ],
            "119": [
                "_67_Ha",
                "Poste",
                "Andavamamba",
                "Ampefiloha",
                "Mahamasina",
                "Ambohijatovo",
                "Antsahabe",
                "Ankatso",
            ],
            "147_Red": [
                "Anosy",
                "Mahamasina",
                "Belair",
                "Besarety",
                "Avaradoha",
                "Meteo",
                "Nanisana",
                "Ankadindramamy",
                "Ambatomaro",
            ],
            "147_Blue": [
                "Anosy",
                "Ambodin_Isotry",
                "_67_Ha",
                "Ankazomanga",
                "Behoririka",
                "Andravoahagny",
                "Besarety",
                "Homi",
                "Meteo",
                "Ampasampito",
                "Ankadindramamy",
                "Ambatomaro",
            ],
            "144": ["Besarety", "Avaradoha", "Ampasampito", "Mahazo", "Ambohimahitsy"],
        }

        self.BUS_STOPS = [
            bus_stop
            for bus, bus_stops in self.BUS.items()
            for bus_stop in set(bus_stops)
        ]

        self.LINKS = [
            ("Ambodin_Isotry", "_67_Ha"),
            ("Art_Malagasy", "Score_digue"),
            ("Antsahabe", "Ankatso"),
            ("Andavamamba", "Ampefiloha"),
            ("Ampefiloha", "Mahamasina"),
            ("_67_Ha", "Poste"),
            ("Meteo", "Ampasampito"),
            ("Andohatapenaka", "_67_Ha"),
            ("Meteo", "Nanisana"),
            ("Mahamasina", "Belair"),
            ("Ankazomanga", "Behoririka"),
            ("Andravoahagny", "Besarety"),
            ("Besarety", "Avaradoha"),
            ("Ambohitrimanjaka", "Tetezana"),
            ("Homi", "Meteo"),
            ("Ampasampito", "Mahazo"),
            ("Besarety", "Homi"),
            ("Tetezana", "Art_Malagasy"),
            ("Ampasampito", "Ankadindramamy"),
            ("Poste", "Andavamamba"),
            ("_67_Ha", "Ankazomanga"),
            ("Behoririka", "Andravoahagny"),
            ("Score_digue", "Andohatapenaka"),
            ("Mahamasina", "Ambohijatovo"),
            ("Anosy", "Mahamasina"),
            ("Ankadindramamy", "Ambatomaro"),
            ("Mahazo", "Ambohimahitsy"),
            ("Anosy", "Ambodin_Isotry"),
            ("Belair", "Besarety"),
            ("Avaradoha", "Meteo"),
            ("Ambohijatovo", "Antsahabe"),
            ("Avaradoha", "Ampasampito"),
            ("Nanisana", "Ankadindramamy"),
        ]

        self.LINKS_DATA = {
            link: {
                "state": random.choice(["good", "bad", "impassable"]),
                "duration": random.randint(5, 10),  # in minutes
            }
            for link in self.LINKS
        }
