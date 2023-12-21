from typing import Any
from data import NOISE
from app.DataSource import DataSource


class DataModel:
    bus: dict[str, list[str]]
    bus_stop_time: dict[str, int]
    link_data: dict[tuple[str, str], dict[str, Any]]
    data_source: DataSource

    def __init__(self, data_source):
        self.data_source = data_source
        self.reset()

    def reset(self):
        self.bus = self.data_source.BUS
        self.links = self.data_source.LINKS
        self.bus_stops = self.data_source.BUS_STOPS
        self.link_data = self.data_source.LINKS_DATA

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
        return set([bse for bss, bse in self.links if bss == bus_stop_start])

    def get_neighbor_node(self, node):
        bus_stop_start, _ = node

        return [
            (bus_stop_end, bus, self.get_time_link((bus_stop_start, bus_stop_end)))
            for bus_stop_end in self.get_neighbor_bus_stop(bus_stop_start)
            for bus in self.get_bus_that_road_on_bus_stop(bus_stop_end)
        ]

    def remove_bus_stop(self, bus_stop):
        # remove in
        # links
        self.links = [
            (bss, bse) for bss, bse in self.links if bss != bus_stop and bse != bus_stop
        ]
        # bus stops
        self.bus_stops = [bs for bs in self.bus_stops if bs == bus_stop]
        # bus
        self.bus = {
            bus: [bs for bs in bus_stops if bs != bus_stop]
            for bus, bus_stops in self.bus.items()
        }
        # link data
        self.link_data = {
            link: data
            for link, data in self.link_data.items()
            if link[0] != bus_stop and link[1] != bus_stop
        }
