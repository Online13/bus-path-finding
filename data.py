import random

# because the node is in this form ["bus_stop", "bus", "change_bus_time", "time"]
NODE_INDEX = {"bus_stop": 0, "bus": 1, "change_bus_time": 2, "time": 3}

NOISE = {"bad": random.randint(0, 30), "impassable": 100, "good": 0}
