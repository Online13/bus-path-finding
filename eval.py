from app.DataModel import DataModel
from app.DataSource import DataSource
from utils import solve, generate_plot
from tqdm import tqdm

# ------------------------------------------

from app.Solver import Solver

if __name__ == "__main__":
    data_source = DataSource()
    # modify data to have more solution
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

    times = []
    for i in tqdm(range(100)):
        time = solve(
            solver, bus_stop_start, bus_stop_end, show_summary=False, verbose=False
        )
        times.append(time)
        generate_plot("out", data_model)

    print("mean times = ", sum(times) / len(times))

    # ------------------------------------------------------------

    solver.data_model.reset()
    solver.make_arc_consistency(bus_stop_start, bus_stop_end)

    times = []
    for i in tqdm(range(100)):
        time = solve(
            solver, bus_stop_start, bus_stop_end, show_summary=False, verbose=False
        )
        times.append(time)
        generate_plot("out-AC", data_model)

    print("mean times = ", sum(times) / len(times))

    # ------------------------------------------
