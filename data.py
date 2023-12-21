import random

random.seed(5)

BUS = {
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

BUS_STOPS = [bus_stop for bus, bus_stops in BUS.items() for bus_stop in set(bus_stops)]

LINKS = [
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

LINKS_DATA = {
    link: {
        "state": random.choice(["good", "bad", "impassable"]),
        "duration": random.randint(5, 10),  # in minutes
    }
    for link in LINKS
}

# because the node is in this form ["bus_stop", "bus", "change_bus_time", "time"]
NODE_INDEX = {"bus_stop": 0, "bus": 1, "change_bus_time": 2, "time": 3}

NOISE = {"bad": random.randint(0, 30), "impassable": 100, "good": 0}
