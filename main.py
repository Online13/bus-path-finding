from app.DataSource import DataSource

data_source = DataSource()

# ------------------------------------------

from app.Solver import Solver

solver = Solver(data_source)
solutions = solver.find_path("Andohatapenaka", "Meteo")
print("solutions=", solutions, end="\n" * 4)
solver.summary(solutions)

# ------------------------------------------

from data import BUS
from app.Visualizer import Visualizer

visualizer = Visualizer("out", data_source=data_source)
visualizer.introduction()
visualizer.plot_graph()
for bus in BUS:
    visualizer.plot_bus_path(bus)
