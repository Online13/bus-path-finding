from app.DataModel import DataModel
from app.DataSource import DataSource
from utils import solve, generate_plot, plot_bus_stop_to_remove

# ------------------------------------------

from app.Solver import Solver

if __name__ == "__main__":
    data_source = DataSource()
    data_source.LINKS_DATA = {
        link: {
            "state": "good",
            "duration": data_source.LINKS_DATA[link]["duration"],  # in minutes
        }
        for link in data_source.LINKS_DATA
    }

    data_model = DataModel(data_source=data_source)

    solver = Solver(data_model)
    bus_stop_start = "Andohatapenaka"
    bus_stop_end = "Meteo"

    # ------------------------------------------------------------

    solve(solver, bus_stop_start, bus_stop_end, verbose=True)
    generate_plot("out", data_model)

    # ------------------------------------------------------------

    solver.data_model.reset()
    bus_stops = solver.make_arc_consistency(bus_stop_start, bus_stop_end)
    plot_bus_stop_to_remove(bus_stops, DataModel(data_source=data_source))

    solve(solver, bus_stop_start, bus_stop_end, show_summary=True, verbose=True)
    generate_plot("out-AC", solver.data_model)

    # ------------------------------------------
