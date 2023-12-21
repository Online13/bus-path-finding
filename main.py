from app.DataSource import DataSource

data_source = DataSource()

# ------------------------------------------

from app.Solver import Solver
from app.Timer import Timer

solver = Solver(data_source)
bus_stop_start = "Andohatapenaka"
bus_stop_end = "Meteo"

with Timer() as timer1:
    solutions = solver.find_path(bus_stop_start, bus_stop_end)
    print("number of possibility = ", len(solutions))
    # solver.summary(solutions)

print()
solver.data_source.reset()
solver.make_arc_consistency(bus_stop_start, bus_stop_end)

with Timer() as timer2:
    solutions = solver.find_path(bus_stop_start, bus_stop_end)
    print("number of possibility = ", len(solutions))

solver.summary(solutions)

# ------------------------------------------

from data import BUS
from app.Visualizer import Visualizer

visualizer = Visualizer("out", data_source=data_source)
visualizer.introduction()
visualizer.plot_graph()
for bus in BUS:
    visualizer.plot_bus_path(bus)
