import os
from .DataModel import DataModel


class Visualizer:
    path_dir: str
    data_model: DataModel

    def __init__(self, path_dir, data_model: DataModel):
        self.path_dir = path_dir
        self.data_model = data_model

    def plot_graph(self):
        with open(f"{self.path_dir}/graph.gv", "+w") as file:
            file.write(f"digraph G {{\n")
            file.write(f'\tlabelloc="t"')
            file.write(f'\tlabel="Environment"')
            for a, b in self.data_model.links:
                weight = self.data_model.get_time_link((a, b))
                file.write(f'\t{a} -> {b} [weight={weight}, label="{weight}"];\n')
            for bus_stop in self.data_model.bus_stops:
                file.write(f"\t{bus_stop};\n")
            file.write("}")
        os.system(f"dot -Tpng {self.path_dir}/graph.gv -o {self.path_dir}/graph.png")

    def plot_bus_path(self, bus: str):
        bus_stops = self.data_model.bus[bus]

        with open(f"{self.path_dir}/bus_{bus}.gv", "+w") as file:
            file.write(f"digraph G {{\n")
            file.write(f'\tlabelloc="t"')
            file.write(f'\tlabel="Itinerary of {bus} Bus"')
            for a, b in self.data_model.links:
                weight = self.data_model.get_time_link((a, b))
                color = (
                    f'[color="blue", weight={weight}, label="{weight}"]'
                    if a in bus_stops and b in bus_stops
                    else f'[weight={weight}, label="{weight}"]'
                )
                file.write(f"\t{a} -> {b} {color};\n")
            for bus_stop in self.data_model.bus_stops:
                if bus_stop in bus_stops:
                    file.write(f'\t{bus_stop} [color="blue", fontcolor="blue"];\n')
                else:
                    file.write(f"\t{bus_stop};\n")
            file.write("}")
        os.system(
            f"dot -Tpng {self.path_dir}/bus_{bus}.gv -o {self.path_dir}/bus_{bus}.png"
        )

    def plot_bus_stop_to_remove(self, bus_stops):
        with open(f"{self.path_dir}/bus_filtering.gv", "+w") as file:
            file.write(f"digraph G {{\n")
            file.write(f'\tlabelloc="t"')
            file.write(f'\tlabel="After filtering"')
            for a, b in self.data_model.links:
                weight = self.data_model.get_time_link((a, b))
                color = (
                    f'[color="red", weight={weight}, label="{weight}"]'
                    if a in bus_stops and b in bus_stops
                    else f'[weight={weight}, label="{weight}"]'
                )
                file.write(f"\t{a} -> {b} {color};\n")
            for bus_stop in self.data_model.bus_stops:
                if bus_stop in bus_stops:
                    file.write(f'\t{bus_stop} [color="red", fontcolor="red"];\n')
                else:
                    file.write(f"\t{bus_stop};\n")
            file.write("}")
        os.system(
            f"dot -Tpng {self.path_dir}/bus_filtering.gv -o {self.path_dir}/bus_filtering.png"
        )

    def introduction(self):
        with open(f"{self.path_dir}/intro.gv", "+w") as file:
            file.write(f"digraph G {{\n")
            file.write(f'\tlabelloc="t"')
            file.write(f'\tlabel="Environment"')
            file.write(f'\t Andohatapenaka [color="blue", fontcolor="blue"];\n')
            file.write(f'\t Meteo [color="blue", fontcolor="blue"];\n')
            for a, b in self.data_model.links:
                weight = self.data_model.get_time_link((a, b))
                file.write(f'\t{a} -> {b} [weight={weight}, label="{weight}"];\n')
            file.write("}")
        os.system(f"dot -Tpng {self.path_dir}/intro.gv -o {self.path_dir}/intro.png")
