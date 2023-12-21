from typing import Any
from data import BUS, LINKS_DATA, LINKS, NOISE, BUS_STOPS


class DataSource:
    bus: dict[str, list[str]]
    bus_stop_time: dict[str, int]
    link_data: dict[tuple[str, str], dict[str, Any]]

    def __init__(self):
        self.bus = BUS
        self.links = LINKS
        self.bus_stops = BUS_STOPS
        self.link_data = LINKS_DATA

    def get_weight_link(self, link: tuple[str, str]):
        return self.link_data[link]

    def get_time_link(self, link: tuple[str, str]):
        weight = self.get_weight_link(link=link)
        state = weight["state"]
        duration = weight["duration"]
        return duration + NOISE[state]

    def get_bus_that_road_on_bus_stop(self, bus_stop: str):
        return [bus for bus, bus_stops in self.bus.items() if bus_stop in bus_stops]

    def get_neighbor_bus_stop(self, bus_stop_start: str):
        neighbors = set()
        for bus, bus_stops in self.bus.items():
            for i, bus_stop in enumerate(bus_stops):
                if bus_stop == bus_stop_start and i + 1 < len(bus_stops):
                    neighbors.add(bus_stops[i + 1])
        return neighbors

    def get_neighbor_node(self, node):
        bus_stop_start, _ = node

        return [
            (bus_stop_end, bus, self.get_time_link((bus_stop_start, bus_stop_end)))
            for bus_stop_end in self.get_neighbor_bus_stop(bus_stop_start)
            for bus in self.get_bus_that_road_on_bus_stop(bus_stop_end)
        ]

    def remove_bus_stop(self, bus_stop):
        pass
